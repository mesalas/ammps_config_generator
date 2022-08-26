import os

from baseconfiguration.base_agent_configuration import *
from configgenerator import configuration_generator
import pandas as pd
from pathlib import Path
from shutil import copyfile, rmtree
import natsort

import datetime
from pandas.tseries.offsets import BDay
import numpy as np


if __name__ == "__main__":
    run_number = 290
    batches = 24

    number_of_days = 261
    config_name = "get from somewhere"
    configs_dir = "configs/"
    if not Path(configs_dir).is_dir():
        Path(configs_dir).mkdir()
    run_dir = ""


    n = 0

    for institution_cash in [250000, 1375000, 2500000]:
        for random_seed in [93457873,23273472,519210238,52524110,
                 7658384,134981,95547732,5635274]:

            np.random.seed(random_seed)
            run_name = str(run_number)+"_"+str(n)+"_instCash-"+str(institution_cash)+"_seed-"+str(random_seed)
            new_config = configuration_generator.ConfigurationWriter(
                config_name=str(run_number)+"_"+str(n),
                seed=random_seed,
                path=configs_dir,
                file_name=run_name+".xlsx" # We may want a different file name than run name
            )
            start_date = "1/1/2017 9:30:00"
            start_date_dt = datetime.datetime.strptime(start_date, "%m/%d/%Y %H:%M:%S")
            end_date_dt = start_date_dt + BDay(number_of_days)
            # start and end dates year, month, day, hour, minute,second
            new_config.add_dates(
                start_date_dt.year, start_date_dt.month, start_date_dt.day, 9, 30, 00,
                end_date_dt.year, end_date_dt.month, end_date_dt.day, 16, 30, 00
            )
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

            n_dls_institutions = 100
            name = "DividendInstitution"
            dividend_longshort_institutions.parameters["initialCash"] = institution_cash
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
            name = "HarkBrokerInstitution"
            hark_broker_isntitution.parameters["brokerSide"] = "BuyTarget"
            buy_broker = hark_broker_isntitution.make_param(np,n=1).to_dict(orient='records')
            hark_broker_isntitution.parameters["brokerSide"] = "SellTarget"
            sell_broker = hark_broker_isntitution.make_param(np,n=1, start_number = 1).to_dict(orient='records')

            new_config.add_agent(
                name=name,
                values=buy_broker+sell_broker
            )
            # Zero info traders
            name = "ZeroInfo"
            n_zi_st = 50
            zi_st_get_flat = zero_info_trader_ST.make_param(np,n=n_zi_st).to_dict(orient='records')
            zero_info_trader_ST.parameters["getFlatOnClose"] = "false"

            agent_values = zi_st_get_flat

            for d in agent_values:
                d["parameter"] = d["triggerSecs"]

            new_config.add_agent(
                name=name,
                values=agent_values
            )


            name = "AggressorTrend"
            new_config.add_agent(
                name=name,
                values=pd.concat([
                    aggressor_traders_ST.make_param(np,n=40),
                    aggressor_traders_LT.make_param(np,n=45)
                ]).to_dict(orient='records')
            )

            name = "BreakoutTrend"
            new_config.add_agent(
                name=name,
                values=pd.concat([
                    breakout_traders_ST.make_param(np,n=40),
                    breakout_traders_LT.make_param(np,n=45)
                ]).to_dict(orient='records')
            )

            name = "RsiReversion"
            new_config.add_agent(
                name=name,
                values=pd.concat([
                    rsireversion_traders_ST.make_param(np,n= 40),
                    rsireversion_traders_LT.make_param(np,n= 40)
                ]).to_dict(orient='records')
            )


            name = "PullbackReversion"
            new_config.add_agent(
                name=name,
                values=pd.concat([
                    pullbackreversion_traders_ST.make_param(np,n= 40)
                    #,
                    #pullbackreversion_traders_LT.make_param(np,n= 50)
                ]).to_dict(orient='records')
            )

            name = "ScalperReversion"
            new_config.add_agent(
                name=name,
                values=pd.concat([
                    scalperreversion_traders_ST.make_param(np,n=40),
                    scalperreversion_traders_LT.make_param(np,n=45)
                ]).to_dict(orient='records')
            )

            new_config.write_file()
            n += 1

    if batches == None: #This will put one file in each batch
        batches = 0

    ### CREATE BATCH FOLDERS ###
    if batches:
        for i in range(1, batches+1):
            batch_dir = run_dir + "batch" + str(i) + "/"
            if not Path(batch_dir).is_dir():
                Path(batch_dir).mkdir()
            if len(os.listdir(batch_dir)) > 0:
                print("{} already contain files\nPlease check it contains the intended configs\n".format(batch_dir))
            # Put shell scripts in the newly created folders
            shellscript = "../../scripts/startsim.sh"
            copyfile(Path(shellscript), Path(batch_dir + "startsim.sh"))

        # Put files in batch folders modularly:
        i = 1
        config_paths = list(Path(configs_dir).glob(str(run_number)+'_*.xlsx'))
        for config in natsort.realsorted(config_paths, key = lambda p : p.name.split("_")[1]):
            batch_dir = run_dir + "batch" + str(i) + "/"
            new_config = batch_dir + config.name
            copyfile(Path(config), Path(new_config))
            i += 1
            if i > batches:
                i = 1

        # Delete empty batch folders
        for i in range(1, batches+1):
            batch_dir = run_dir + "batch" + str(i) + "/"
            if not len(list(Path(batch_dir).glob('*.xlsx'))):
                rmtree( Path(batch_dir) )
