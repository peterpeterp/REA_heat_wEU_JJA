import sys
import xarray as xr
import numpy as np
sys.path.append('../../')
from experiment_configuration.regions.region_by_slice import create_or_load_regional_mask, regional_average, shift_lon

name_addition = '-reg'
preprocessing_attr = 'regional average over region of interest'

dummy_exp = experiment(importlib.import_module(f"experiment_configuration.{experiment_identifier}").config)

def preprocessor(nc):
    nc = shift_lon(nc)
    obs = nc[dummy_exp.observable_of_interest] - 273.15
    obs = regional_average(obs, dummy_exp.regional_mask)
    return obs