import sys
sys.path.append('../..')

from acg.configgenerator import configuration_generator
from acg.baseconfiguration.portfolio_test_sim_configuration import *

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
parser.add_argument("--zi-scaler", dest = "ZI_n_scaler", type = float, default=1.0, help = "scaling factor scaling the number of Zi agnets",required=True )
parser.add_argument("--zi-tp-max", dest = "zi_tp_max", type = float, default=1.0, help = "value for take profit for Zi agnets",required=True )
parser.add_argument("--portfolio-update-pct", dest = "portfolio_update_pct", type = float, default=1.0, help = "Prob for new portfolio on new EPS",required=True )

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
        values=marketmaker_traders.make_param(np,9).to_dict(orient='records')
    )

    # Zero info traders
    name = "ZeroInfo"
    n_zi_st = 100*args.ZI_n_scaler

    zero_info_trader_ST.parameters["stopMultiplier"] = [0.5, args.zi_tp_max, True]
    zi_st_get_flat = zero_info_trader_ST.make_param(np,n=n_zi_st).to_dict(orient='records')

    agent_values = zi_st_get_flat

    for d in agent_values:
        d["parameter"] = d["triggerSecs"]

    new_config.add_agent(
        name=name,
        values=agent_values
    )

    name = "PortfolioTrader"
    portfolio_trader.parameters["updateOnEarningsPct"] = args.portfolio_update_pct
    new_config.add_agent(
        name=name,
        values=
            portfolio_trader.make_param(np,n=100).to_dict(orient='records')
    )

    new_config.write_file()


