import os,sys,subprocess,glob,importlib
from datetime import datetime
import xarray as xr
import numpy as np
import pandas as pd

# get some paths and general settings
sys.path.append('/home/u/u290372/projects/REA_with_CESM2')
from REA_launcher import launch_handler


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--experiment", type=str)
    parser.add_argument("--verbose", action='store_true')
    parser.add_argument("--dry_run", action='store_true')
    parser.add_argument("--relaunch_cases_which_are_unclear", action='store_true')
    parser.add_argument("--relaunch_after_completion", action='store_true')
    command_line_arguments = parser.parse_args()

    # load configuration settings
    chosen_experiment_configuration = importlib.import_module(f"experiment_configuration.{command_line_arguments.experiment}")
    
    # finalize experiment configuration
    from experiment_configuration.experiment import experiment
    exp = experiment(chosen_experiment_configuration.config)

    launcher = launch_handler(
        exp, 
        verbose=command_line_arguments.verbose, 
        dry_run=command_line_arguments.dry_run, 
        relaunch_cases_which_are_unclear=command_line_arguments.relaunch_cases_which_are_unclear, 
        relaunch_after_completion=command_line_arguments.relaunch_after_completion
        )

    launcher.do_what_has_to_be_done()