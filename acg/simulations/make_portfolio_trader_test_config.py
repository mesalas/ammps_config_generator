import sys
sys.path.append('../..')

from acg.configgenerator import configuration_generator
from acg.baseconfiguration.base_agent_configuration import *

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
parser.add_argument("--portfolio-trader-int-vol", dest="portfolio_trader_int_vol", type = float, help = "initial value for the porfilio traders volatility",required=True)

def make_portfolio_trader_test(random_seed, run_name, config_dir, portfolio_trader_int_vol):

    np.random.seed(random_seed)

    new_config = configuration_generator.ConfigurationWriter(
        config_name=run_name,
        seed=random_seed,
        path=config_dir,
        file_name=run_name # We may want a different file name than run name
    )
    start_date = "1/1/2017 9:30:00"
    start_date_dt = datetime.datetime.strptime(start_date, "%m/%d/%Y %H:%M:%S")
    end_date_dt = start_date_dt + BDay(260)
    # start and end dates year, month, day, hour, minute,second
    new_config.add_dates(
        start_date_dt.year, start_date_dt.month, start_date_dt.day, 9, 30, 00,
        end_date_dt.year, end_date_dt.month, end_date_dt.day, 16, 30, 00
    )

    new_config.add_agent(
        name=marketmaker_traders.name,
        values=marketmaker_traders.make_param(np,9).to_dict(orient='records')
    )

    # Zero info traders
    name = "ZeroInfo"
    n_zi_st = 30
    zero_info_trader_ST.parameters["parameterMin"] = 600
    zero_info_trader_ST.parameters["parameterMax"] = 3600
    zero_info_trader_ST.parameters["ziReversionFactor"] = 0.5

    zi_st_get_flat = zero_info_trader_ST.make_param(np,n=n_zi_st).to_dict(orient='records')
    zero_info_trader_ST.parameters["getFlatOnClose"] = "true"

    agent_values = zi_st_get_flat

    for d in agent_values:
        d["parameter"] = d["triggerSecs"]
        d["agentSymbols"] = "ABC,DEF,GHI"

    new_config.add_agent(
        name=name,
        values=agent_values
    )

    name = "PortfolioTrader"
    portfolio_trader.parameters["initialVol"] = portfolio_trader_int_vol
    new_config.add_agent(
        name=name,
        values=
            portfolio_trader.make_param(np,n=100).to_dict(orient='records')
    )

    new_config.write_file()


if __name__ == "__main__":
    args = parser.parse_args()
    args_string = ""
    for i in range(1,len(sys.argv)):
        args_string = args_string + " " + sys.argv[i]
    print("Started with the following arguments:", args_string)

    make_portfolio_trader_test(args.seed,args.run_name,args.conf_dir,args.portfolio_trader_int_vol)

