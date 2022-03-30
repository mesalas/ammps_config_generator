from baseconfiguration.base_agent_configuration import *
from configgenerator import configuration_generator
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("--out-dir", dest="conf_dir", type = str, help = "output directory")
parser.add_argument("--name", dest="run_name", type = str, help= "name of simulation in ammps")
parser.add_argument("--seed", dest="seed", type = int, help = "random seed")
if __name__ == "__main__":

    args = parser.parse_args()
    random_seed = args.seed
    run_name = args.run_name
    config_name = "get from somewhere"

    config_dir = args.conf_dir
    new_config = configuration_generator.ConfigurationWriter(
        config_name=run_name,
        seed=random_seed,
        path=config_dir,
        file_name=run_name # We may want a different file name than run name
    )

    # start and end dates year, month, day, hour, minute,second
    new_config.add_dates(
        2017, 1, 1, 9, 30, 00,
        2018, 1, 1, 16, 30, 00
    )
    new_config.add_agent(
        name=marketmaker_traders.name,
        values=marketmaker_traders.make_param(9).to_dict(orient='records')
    )

    # Pairtraders
    agent_values = pair_traders.make_param(35).to_dict(orient='records')
    for d in agent_values:
        d["lookbackPeriods"] = int(d["horizon"] / d["updateInterval"])

    new_config.add_agent(
        name=pair_traders.name,
        values=agent_values

    )

    n_ls_institutions = 500
    name = "LongShortInstitution"
    if n_ls_institutions > 0:
        new_config.add_agent(
            name=name,
            values=longshort_institutions_LT.make_param(n_ls_institutions).to_dict(
                orient='records')
        )

    name = "SectorRotateInstitution"

    new_config.add_agent(
        name=name,
        values=sectorrotate_institution_LT.make_param(n= 50).to_dict(orient='records')
    )

    # Zero info traders
    name = "ZeroInfo"
    n_zi_st = 50
    zi_st_get_flat = zero_info_trader_ST.make_param(n=n_zi_st).to_dict(orient='records')
    zero_info_trader_ST.parameters["getFlatOnClose"] = "false"
    zi_st_no_get_flat = zero_info_trader_ST.make_param(n=n_zi_st, start_number=n_zi_st, name_suffix="noFlat").to_dict(
        orient='records')

    agent_values = zi_st_get_flat + zi_st_no_get_flat

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
            aggressor_traders_ST.make_param(n=20),
            aggressor_traders_LT.make_param(n=45)
        ]).to_dict(orient='records')
    )

    name = "BreakoutTrend"
    new_config.add_agent(
        name=name,
        values=pd.concat([
            breakout_traders_ST.make_param(n=20),
            breakout_traders_LT.make_param(n=45)
        ]).to_dict(orient='records')
    )

    name = "RsiReversion"
    new_config.add_agent(
        name=name,
        values=pd.concat([
            rsireversion_traders_ST.make_param(n= 25),
            rsireversion_traders_LT.make_param(n= 40)
        ]).to_dict(orient='records')
    )


    name = "PullbackReversion"
    new_config.add_agent(
        name=name,
        values=pd.concat([
            pullbackreversion_traders_ST.make_param(n= 30),
            pullbackreversion_traders_LT.make_param(n= 50)
        ]).to_dict(orient='records')
    )

    name = "ScalperReversion"
    new_config.add_agent(
        name=name,
        values=pd.concat([
            scalperreversion_traders_ST.make_param(n=20),
            scalperreversion_traders_LT.make_param(n=40)
        ]).to_dict(orient='records')
    )

    new_config.write_file()


