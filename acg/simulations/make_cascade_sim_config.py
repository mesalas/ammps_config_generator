import sys
sys.path.append('../..')

from acg.configgenerator import configuration_generator
from acg.baseconfiguration.basic_trader_test_configuration import *
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
parser.add_argument("--n-basic-trader", dest = "n_basic_trader", type = float, default=1.0, help = "scaling the number of basic trader agnets",required=True )
parser.add_argument("--algo-cash-scaler", dest = "algo_cash_scaler", type = float, default=1.0, help = "scaling factor scaling cash for algo/intraday agents",required=True )


if __name__ == "__main__":

    args = parser.parse_args()
    args_string = ""
    for i in range(1,len(sys.argv)):
        args_string = args_string + " " + sys.argv[i]
    print("Started with the following arguments:", args_string)
    number_of_days = args.number_of_days
    config_name = "get from somewhere"
    np.random.seed(args.seed)

    new_config = configuration_generator.ConfigurationWriter(
        config_name=args.run_name,
        seed=args.seed,
        path=args.conf_dir,
        file_name=args.run_name # We may want a different file name than run name
    )
    start_date = "1/1/2017 9:30:00"
    start_date_dt = datetime.datetime.strptime(start_date, "%m/%d/%Y %H:%M:%S")
    end_date_dt = start_date_dt + BDay(number_of_days)
    # start and end dates year, month, day, hour, minute,second
    new_config.add_dates(
        start_date_dt.year, start_date_dt.month, start_date_dt.day, 9, 30, 00,
        end_date_dt.year, end_date_dt.month, end_date_dt.day, 16, 30, 00
    )

    name = "MarketMaker"
    new_config.add_agent(
        name=name,
        values=marketmaker_traders.make_param(np,6).to_dict(orient='records')
    )
    # Basic traders
    name = "BasicTrader"
    basic_traders = basic_trader.make_param(np,n=int(125*args.n_basic_trader)).to_dict(orient='records')


    agent_values = basic_traders
    new_config.add_agent(
        name=name,
        values=agent_values
    )
    name = "AggressorTrend"
    aggressor_traders_ST.parameters["initialCash"] = aggressor_traders_ST.parameters["initialCash"] * args.algo_cash_scaler



    new_config.add_agent(
        name=name,
        values=pd.concat([
            aggressor_traders_ST.make_param(np,n=100)
        ]).to_dict(orient='records')
    )

    name = "BreakoutTrend"
    breakout_traders_ST.parameters["initialCash"] = breakout_traders_ST.parameters["initialCash"] * args.algo_cash_scaler


    new_config.add_agent(
        name=name,
        values=pd.concat([
            breakout_traders_ST.make_param(np,n=100)
        ]).to_dict(orient='records')
    )

    name = "RsiReversion"
    rsireversion_traders_ST.parameters["initialCash"] = rsireversion_traders_ST.parameters["initialCash"] * args.algo_cash_scaler

    new_config.add_agent(
        name=name,
        values=pd.concat([
            rsireversion_traders_ST.make_param(np,n=100)
        ]).to_dict(orient='records')
    )

    name = "ScalperReversion"
    scalperreversion_traders_ST.parameters["initialCash"] = scalperreversion_traders_ST.parameters["initialCash"] * args.algo_cash_scaler

    new_config.add_agent(
        name=name,
        values=pd.concat([
            scalperreversion_traders_ST.make_param(np,n=100)
        ]).to_dict(orient='records')
    )

    new_config.write_file()


