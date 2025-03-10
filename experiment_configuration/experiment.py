import sys,os,glob,importlib
import numpy as np
from experiment_configuration.regions.region_by_slice import create_or_load_regional_mask, regional_average, shift_lon

class experiment():
    def __init__(self, config):
        # general settings
        self.dkrz_project = 'bb1152'
        self.dir_scripts=f"/work/bb1152/u290372/cesm215/cime/scripts"
        self.dir_run=f"/scratch/u/u290372/cesm215_output"
        self.dir_work=f"/work/bb1152/u290372"
        self.dir_repo=f"/home/u/u290372/projects/cesm215_peters_scripts/"

        # launching script
        self.launching_script = "/home/u/u290372/projects/cesm215_peters_scripts/branch_perturbed.py"

        # perturbation method and order of magnitude
        self.perturbation_order_of_magnitude = -13
        self.perturbation_type = 'PT_direct'

        # experiment name
        self.product_name = "heat_wEU_JJA"

        # length of simulation steps
        self.n_days = 5

        # number of steps
        self.n_steps = 18

        # observable of interest
        self.observable_of_interest = 'TREFHT'

        # region of interest
        self.region_of_interest = 'wEU'

        # CESM2 output to save
        self.output = 'gklt_summer'

        # add variables from specific configuration
        for k,v in config.__dict__.items():
            self.__dict__[k] = v

        # start date in year
        self.start_date_in_year = '05-31'

        ini_config_module = importlib.import_module(f"experiment_configuration.initial_conditions.{self.initial_conditions_name}")
        ini_config = ini_config_module.initial_condition_config(self.start_date_in_year)
        for k,v in ini_config.__dict__.items():
            self.__dict__[k] = v        



        assert self.n_members == 42*3, \
            f"the number of initial conditions has changed: expected=42*3 got={self.n_members}"

        # experiment name
        self.experiment_name = f"{self.region_of_interest}.{self.observable_of_interest}.{self.start_date_in_year}.{self.n_days}x{self.n_steps}.{self.initial_conditions_name}.k{str(self.k).replace('.','p')}.s{self.seed}"

        # regional mask
        self.regional_mask = create_or_load_regional_mask(
            regional_mask_file = f"{self.dir_work}/GKLT/regions/{self.region_of_interest}.nc",
            slice_lat=slice(44,55), 
            slice_lon=slice(-4,12),
            )

        # template dict for todos
        # the dict will later be transformed to command line arguments for the launching script
        self.launch_template = {
            "dkrz_project" : self.dkrz_project,
            "case_identifier" : "",
            "case_path" : "",
            "parent_path" : "",
            "precompiled_path" : "",
            "perturbation_seed" : "",
            "compset" : self.compset,
            "ndays" : self.n_days,
            "perturbation_type" : self.perturbation_type,
            "perturbation_order_of_magnitude" : self.perturbation_order_of_magnitude,
            "output" : self.output,
        }

        self.dir_archive=f"/work/{self.dkrz_project}/u290372/cesm215_archive"
        self.dir_out = f"{self.dir_work}/GKLT/{self.experiment_name}"
        self.dir_archive_post = f"{self.dir_archive}/GKLT/{self.experiment_name}"

    def get_main_observable(self, nc):
        nc = shift_lon(nc)
        obs = nc[self.observable_of_interest] - 273.15
        obs = regional_average(obs, self.regional_mask)
        return obs

    def calc_score(self, x):
        return float(np.exp(self.k * x.sum()))




