#!/bin/bash

#SBATCH --job-name=launch_resimulate_initial      # Specify job name
#SBATCH --partition=compute     # Specify partition name
#SBATCH --ntasks=1             # Specify max. number of tasks to be invoked
#SBATCH --cpus-per-task=1     # Specify number of CPUs per task
#SBATCH --time=04:00:00        # Set a limit on the total run time
#SBATCH --account=bb1152       # Charge resources on this project account
#SBATCH --output=log/%j    # File name for standard output
#SBATCH --error=log/%j    # File name for standard error output

python /home/u/u290372/projects/REA_with_CESM2/branch_perturbed.py --dkrz_project bb1152 --case_identifier 001_0501 --case_path GKLT/initial_piControl --parent_path /work/bb1445/u290372/cesm215_archive/b.e215.B1850cmip6.f09_g17.001.fE.0500.ens000/branch/0501-01-01_to_0501-04-30/branch/0501-04-30_to_0501-05-31 --perturbation_seed 0 --compset B1850cmip6 --ndays 90 --output gklt_summer --precompiled_path GKLT/initial_piControl/001_0510/ --overwrite 
python /home/u/u290372/projects/REA_with_CESM2/branch_perturbed.py --dkrz_project bb1152 --case_identifier 001_0504 --case_path GKLT/initial_piControl --parent_path /work/bb1445/u290372/cesm215_archive/b.e215.B1850cmip6.f09_g17.001.fE.0500.ens000/branch/0504-01-01_to_0504-04-30/branch/0504-04-30_to_0504-05-31 --perturbation_seed 0 --compset B1850cmip6 --ndays 90 --output gklt_summer --precompiled_path GKLT/initial_piControl/001_0510/ --overwrite 
python /home/u/u290372/projects/REA_with_CESM2/branch_perturbed.py --dkrz_project bb1152 --case_identifier 001_0507 --case_path GKLT/initial_piControl --parent_path /work/bb1445/u290372/cesm215_archive/b.e215.B1850cmip6.f09_g17.001.fE.0500.ens000/branch/0507-01-01_to_0507-04-30/branch/0507-04-30_to_0507-05-31 --perturbation_seed 0 --compset B1850cmip6 --ndays 90 --output gklt_summer --precompiled_path GKLT/initial_piControl/001_0510/ --overwrite 


python /home/u/u290372/projects/REA_with_CESM2/branch_perturbed.py --dkrz_project bb1152 --case_identifier 001_0855 --case_path GKLT/initial_piControl --parent_path /work/bb1445/u290372/cesm215_archive/b.e215.B1850cmip6.f09_g17.001.fE.0500.ens000/branch/0855-01-01_to_0855-04-30/branch/0855-04-30_to_0855-05-31 --perturbation_seed 0 --compset B1850cmip6 --ndays 90 --output gklt_summer --precompiled_path GKLT/initial_piControl/001_0510/ --overwrite 
