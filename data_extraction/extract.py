import os,sys,subprocess,glob,cftime,importlib,pickle,itertools
from datetime import datetime
import xarray as xr
import numpy as np
sys.path.append('../')

sys.path.append('../../REA_with_CESM2')
from ensembles.ensemble_GKLT import ensemble_GKLT
from data_extractor.data_extractor import extract_rea,extract_initial

from experiment_configuration.experiment import experiment

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--variable", type=str)
parser.add_argument("--realm", type=str)
parser.add_argument("--h_identifier", type=str)
parser.add_argument("--time_frequency", type="day")
parser.add_argument("--preprocessing", type=str, default='')
parser.add_argument("--overwrite", action='store_true')
command_line_arguments = parser.parse_args()

for k,v in vars(parser.parse_args()).items():
    globals()[k] = v

if preprocessing == '':
    preprocessing_module = None
else:
    preprocessing_module = importlib.import_module(f"preprocessing.{preprocessing}")

for experiment_identifier in [f"c{i}" for i in range(1,6)] + [f"p{i}" for i in range(1,6)]:
    print(experiment_identifier)
    # load experiment configuration settings
    exp = experiment(importlib.import_module(f"experiment_configuration.{experiment_identifier}").config)

    extract_rea(
        exp,
        variable = variable,
        realm = realm,
        h_identifier = h_identifier,
        time_frequency = time_frequency,
        preprocessing_module = preprocessing_module,
        overwrite = overwrite,
    )

    if '1' in experiment_identifier:
        extract_initial(
            exp,
            variable = variable,
            realm = realm,
            h_identifier = h_identifier,
            time_frequency = time_frequency,
            preprocessing_module = preprocessing_module,
            overwrite = overwrite,
        )
    