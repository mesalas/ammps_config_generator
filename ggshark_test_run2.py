from make_ggshark_config import make_ggshark
import pandas as pd
public_fractions = [1.0,1.0,1.0]
random_seeds = [594271,
369251,
681561,
100227,
363555,
622405,
56882,
680939,
270613]
# seeds from https://numbergenerator.org/random-9-digit-number-generator#!numbers=9&length=6&addfilters=
n = 0
number_of_days = 260
conf_dir = "ggshark_test2"

sim_numbers = []
run_names = []
public_fractions_list = []
for seed in random_seeds:
    for public_fraction in public_fractions:
        run_name = "ggshark_test_run2_" + str(n) + ".xlsx"
        make_ggshark(seed,run_name,number_of_days,conf_dir,public_fraction)
        sim_numbers.append(n)
        run_names.append(run_name)
        public_fractions_list.append(public_fraction)
        n+= 1


output_table = {"n" : sim_numbers, "run names" : run_names, "public fraction" : public_fractions_list}
pd.DataFrame(output_table).to_csv("ggshark_test_run_params.csv")
