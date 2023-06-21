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
parser.add_argument("--portfolio-update-pct", dest = "portfolio_update_pct", type = float, default=1.0, help = "Prob for new portfolio on new EPS",required=True )
parser.add_argument("--n-portfolio-investors",dest = "n_portfolio_investors",type = float)
parser.add_argument("--rebalance-threshold-max", dest = "rebalance_threshold_max",type = float)
parser.add_argument("--update-portfolio-threshold_max", dest = "update_portfolio_threshold_max",type = float)

if __name__ == "__main__":
    args = parser.parse_args()
    args_string = ""
    for i in range(1,len(sys.argv)):
        args_string = args_string + " " + sys.argv[i]
    print("Started with the following arguments:", args_string)

    np.random.seed(args.seed)

    new_config = configuration_generator.ConfigurationWriter(
        config_name=args.run_name,
        seed=args.seed,
        path=args.conf_dir,
        file_name=args.run_name # We may want a different file name than run name
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
        values=marketmaker_traders.make_param(np,3).to_dict(orient='records')
    )

    # Basic traders
    name = "BasicTrader"
    basic_traders = basic_trader.make_param(np,n=250).to_dict(orient='records')


    agent_values = basic_traders
    new_config.add_agent(
        name=name,
        values=agent_values
    )

    name = "PortfolioTrader"
    portfolio_trader.parameters["updateOnEarningsPct"] = args.portfolio_update_pct
    portfolio_trader.parameters["rebalanceThresholdMin"] = 0.0
    portfolio_trader.parameters["rebalanceThresholdMax"] = args.rebalance_threshold_max
    portfolio_trader.parameters["updatePortfolioThresholdMin"] = 0.0
    portfolio_trader.parameters["updatePortfolioThresholdMax"] = args.update_portfolio_threshold_max
    new_config.add_agent(
        name=name,
        values=
            portfolio_trader.make_param(np,n=args.n_portfolio_investors).to_dict(orient='records')
    )

    new_config.write_file()


