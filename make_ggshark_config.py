from baseconfiguration.base_agent_configuration import *
from configgenerator import configuration_generator
import pandas as pd
import argparse
import datetime
from pandas.tseries.offsets import BDay
import numpy as np
import sys

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("--out-dir", dest="conf_dir", default = "",type = str, help = "output directory")
parser.add_argument("--name", dest="run_name", type = str, help= "name of simulation in ammps", required=True)
parser.add_argument("--seed", dest="seed", type = int, help = "random seed",required=True)
parser.add_argument("--days", dest="number_of_days", type = int, default = 261, help = "days to simulate")

if __name__ == "__main__":

    args = parser.parse_args()
    args_string = ""
    for i in range(1,len(sys.argv)):
        args_string = args_string + " " + sys.argv[i]
    print("Started with the following arguments:", args_string)
    random_seed = args.seed
    run_name = args.run_name
    number_of_days = args.number_of_days
    config_name = "get from somewhere"
    np.random.seed(random_seed)

    config_dir = args.conf_dir
    new_config = configuration_generator.ConfigurationWriter(
        config_name=run_name,
        seed=random_seed,
        path=config_dir,
        file_name=run_name # We may want a different file name than run name
    )
    start_date = "1/1/2017 9:30:00"
    start_date_dt = datetime.datetime.strptime(start_date, "%m/%d/%Y %H:%M:%S")
    end_date_dt = start_date_dt + BDay(number_of_days)
    # start and end dates year, month, day, hour, minute,second
    new_config.add_dates(
        start_date_dt.year, start_date_dt.month, start_date_dt.day, 9, 30, 00,
        end_date_dt.year, end_date_dt.month, end_date_dt.day, 16, 30, 00
    )
    marketmaker_traders.parameters["workSize"] = 150
    new_config.add_agent(
        name=marketmaker_traders.name,
        values=marketmaker_traders.make_param(np,9).to_dict(orient='records')
    )

    # No pairs to be traded in a single instrument sim
    # # Pairtraders
    # agent_values = pair_traders.make_param(np,35).to_dict(orient='records')
    # for d in agent_values:
    #     d["lookbackPeriods"] = int(d["horizon"] / d["updateInterval"])
    #
    # new_config.add_agent(
    #     name=pair_traders.name,
    #     values=agent_values
    #
    # )

    n_dls_institutions = 50
    name = "DividendInstitution"
    if n_dls_institutions > 0:
        new_config.add_agent(
            name=name,
            values=dividend_longshort_institutions.make_param(np,n_dls_institutions).to_dict(
                orient='records')
        )

    # name = "SectorRotateInstitution"
    #
    # new_config.add_agent(
    #     name=name,
    #     values=sectorrotate_institution_LT.make_param(np,n= 50).to_dict(orient='records')
    # )

    # HarkBroker
    name = "HarkBrokerInstitutionTwoVenue"
    hark_broker_two_venue_institution.parameters["brokerSide"] = "BuyTarget"
    buy_broker = hark_broker_two_venue_institution.make_param(np, n=1).to_dict(orient='records')
    hark_broker_two_venue_institution.parameters["brokerSide"] = "SellTarget"
    sell_broker = hark_broker_two_venue_institution.make_param(np, n=1, start_number = 1).to_dict(orient='records')

    new_config.add_agent(
        name=name,
        values=buy_broker+sell_broker
    )
    # Zero info traders
    name = "ZeroInfo"
    n_zi_st = 30
    zi_st_get_flat = zero_info_trader_ST.make_param(np,n=n_zi_st).to_dict(orient='records')
    zero_info_trader_ST.parameters["getFlatOnClose"] = "false"

    agent_values = zi_st_get_flat

    for d in agent_values:
        d["parameter"] = d["triggerSecs"]

    new_config.add_agent(
        name=name,
        values=agent_values
    )

    new_config.add_agent(
        name=internal_marketmaker.name,
        values=internal_marketmaker.make_param(np,1).to_dict(orient='records')
    )

    name = "AggressorTrend"
    new_config.add_agent(
        name=name,
        values=pd.concat([
            #aggressor_traders_ST.make_param(np,n=40),
            aggressor_traders_LT.make_param(np,n=45)
        ]).to_dict(orient='records')
    )

    # name = "BreakoutTrend"
    # new_config.add_agent(
    #     name=name,
    #     values=pd.concat([
    #         breakout_traders_ST.make_param(np,n=40),
    #         breakout_traders_LT.make_param(np,n=45)
    #     ]).to_dict(orient='records')
    # )

    name = "RsiReversion"
    new_config.add_agent(
        name=name,
        values=pd.concat([
            #rsireversion_traders_ST.make_param(np,n= 40),
            rsireversion_traders_LT.make_param(np,n= 45)
        ]).to_dict(orient='records')
    )


    # name = "PullbackReversion"
    # new_config.add_agent(
    #     name=name,
    #     values=pd.concat([
    #         pullbackreversion_traders_ST.make_param(np,n= 40)
    #         #,
    #         #pullbackreversion_traders_LT.make_param(np,n= 50)
    #     ]).to_dict(orient='records')
    # )
    #
    # name = "ScalperReversion"
    # new_config.add_agent(
    #     name=name,
    #     values=pd.concat([
    #         scalperreversion_traders_ST.make_param(np,n=40),
    #         scalperreversion_traders_LT.make_param(np,n=45)
    #     ]).to_dict(orient='records')
    # )

    new_config.write_file()


