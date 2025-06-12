#!/bin/bash

#SBATCH --job-name=sim_launcher      # Specify job name
#SBATCH --partition=compute     # Specify partition name
#SBATCH --ntasks=1             # Specify max. number of tasks to be invoked
#SBATCH --cpus-per-task=1     # Specify number of CPUs per task
#SBATCH --time=04:00:00        # Set a limit on the total run time
#SBATCH --account=bb1445       # Charge resources on this project account
#SBATCH --output=log/%j    # File name for standard output
#SBATCH --error=log/%j    # File name for standard error output

module purge
module load subversion python3/2022.01-gcc-11.2.0 esmf/8.2.0-intel-2021.5.0
module load esmf/8.2.0-intel-2021.5.0 gcc intel-oneapi-compilers/2022.0.1-gcc-11.2.0 intel-oneapi-mkl/2022.0.1-gcc-11.2.0
module load openmpi/4.1.2-intel-2021.5.0
module load cdo nco python3/2022.01-gcc-11.2.0
module load nano emacs ncview tree

"$@"