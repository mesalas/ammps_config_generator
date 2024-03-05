import sys
sys.path.append('../..')

from acg.configgenerator import configuration_generator
from acg.baseconfiguration.new_agent_configuration import *

import argparse
import datetime
from pandas.tseries.offsets import BDay
import numpy as np
import sys

parser = argparse.ArgumentParser(description='')
parser.add_argument("--out-dir", dest="conf_dir", default = "",type = str, help = "output directory")
parser.add_argument("--name", dest="run_name", type = str, help= "name of simulation in ammps", required=True)
parser.add_argument("--seed", dest="seed", type = int, help = "random seed",required=True)
parser.add_argument("--days", dest="number_of_days", type = int, default = 500, help = "days to simulate")



def make_new_market_config(random_seed, run_name, number_of_days, config_dir):

    np.random.seed(random_seed)

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


    new_config.add_agent(
        name=marketmaker_traders.name,
        values=marketmaker_traders.make_param(np,6).to_dict(orient='records')
    )

    new_config.add_agent(
        name=portfolio_trader.name,
        values=portfolio_trader.make_param(np,1000).to_dict(orient='records')
    )

    new_config.add_agent(
        name=eps_portfolio_trader.name,
        values=eps_portfolio_trader.make_param(np,100).to_dict(orient='records')
    )

    new_config.add_agent(
        name=technical_traders.name,
        values=technical_traders.make_param(np,500).to_dict(orient='records')
    )

    new_config.add_agent(
        name=pair_traders.name,
        values=pair_traders.make_param(np,10).to_dict(orient='records')
    )


    new_config.write_file()


if __name__ == "__main__":
    args = parser.parse_args()
    args_string = ""
    for i in range(1,len(sys.argv)):
        args_string = args_string + " " + sys.argv[i]
    print("Started with the following arguments:", args_string)

    make_new_market_config(args.seed,args.run_name,args.number_of_days,args.conf_dir)

