import sys
sys.path.append('../..')

from acg.configgenerator import configuration_generator
from acg.baseconfiguration.new_agent_configuration import *

import argparse
import datetime
from pandas.tseries.offsets import BDay
import numpy as np

# Update the parser with new arguments
parser = argparse.ArgumentParser(description='')
parser.add_argument("--out-dir", dest="conf_dir", default="", type=str, help="output directory")
parser.add_argument("--name", dest="run_name", type=str, help="name of simulation in ammps", required=True)
parser.add_argument("--seed", dest="seed", type=int, help="random seed", required=True)
parser.add_argument("--days", dest="number_of_days", type=int, default=500, help="days to simulate")
# New parameters for trader numbers and experiment parameters
parser.add_argument("--num-marketmakers", dest="num_marketmakers", type=int, default=6, help="Number of market makers")
parser.add_argument("--num-portfolio-traders", dest="num_portfolio_traders", type=int, default=1000, help="Number of portfolio traders")
parser.add_argument("--num-eps-traders", dest="num_eps_traders", type=int, default=100, help="Number of EPS portfolio traders")
parser.add_argument("--num-technical-traders", dest="num_technical_traders", type=int, default=500, help="Number of technical traders")
parser.add_argument("--num-pair-traders", dest="num_pair_traders", type=int, default=10, help="Number of pair traders")
# Experiment parameters
parser.add_argument("--rebalance-factor-rpt", dest="rebalance_factor_rpt", type=float, default=5.0, help="Rebalance factor for Random Portfolio Traders")
parser.add_argument("--rebalance-factor-eps", dest="rebalance_factor_eps", type=float, default=5.0, help="Rebalance factor for EPS Portfolio Investors")
parser.add_argument("--update-threshold", dest="update_threshold", type=float, default=2.5, help="Update threshold for EPS Portfolio Investors")
parser.add_argument("--inventory-factor", dest="inventory_factor", type=float, default=2.5, help="Inventory factor for Market Makers")

def make_new_market_config(args):
    np.random.seed(args.seed)

    new_config = configuration_generator.ConfigurationWriter(
        config_name=args.run_name,
        seed=args.seed,
        path=args.conf_dir,
        file_name=args.run_name  # We may want a different file name than run name
    )
    start_date = "1/1/2017 9:30:00"
    start_date_dt = datetime.datetime.strptime(start_date, "%m/%d/%Y %H:%M:%S")
    end_date_dt = start_date_dt + BDay(args.number_of_days)
    new_config.add_dates(
        start_date_dt.year, start_date_dt.month, start_date_dt.day, 9, 30, 0,
        end_date_dt.year, end_date_dt.month, end_date_dt.day, 16, 30, 0
    )

    # Use args to pass the number of traders
    marketmaker_traders.parameters["instrumentFactor"]  = args.inventory_factor
    new_config.add_agent(
        name=marketmaker_traders.name,
        values=marketmaker_traders.make_param(np, args.num_marketmakers).to_dict(orient='records')  # Adjusted to pass inventory_factor
    )

    portfolio_trader.parameters["updatePortfolioThresholdMax"] = args.rebalance_factor_rpt
    new_config.add_agent(
        name=portfolio_trader.name,
        values=portfolio_trader.make_param(np, args.num_portfolio_traders).to_dict(orient='records')  # Adjusted to pass rebalance_factor_rpt
    )

    eps_portfolio_trader.parameters["updatePortfolioThresholdMax"] = args.rebalance_factor_eps
    eps_portfolio_trader.parameters["earningsZscoreThreshold"] = args.update_threshold
    new_config.add_agent(
        name=eps_portfolio_trader.name,
        values=eps_portfolio_trader.make_param(np, args.num_eps_traders).to_dict(orient='records')  # Adjusted to pass rebalance_factor_eps and update_threshold
    )

    new_config.add_agent(
        name=technical_traders.name,
        values=technical_traders.make_param(np, args.num_technical_traders).to_dict(orient='records')
    )

    new_config.add_agent(
        name=pair_traders.name,
        values=pair_traders.make_param(np, args.num_pair_traders).to_dict(orient='records')
    )

    new_config.write_file()

if __name__ == "__main__":
    args = parser.parse_args()
    args_string = " ".join(sys.argv[1:])
    print("Started with the following arguments:", args_string)

    make_new_market_config(args)
