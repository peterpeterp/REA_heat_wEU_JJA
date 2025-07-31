#!/bin/bash

cd ../../REA_with_CESM2/data_extractor

ID=$1

python ../../REA_with_CESM2/data_extractor/extract.py --realm atm --h_identifier h2 --variable SHFLX --preprocessing regional_average --project_path ../../REA_heat_wEU_JJA/ --experiment_identifiers $ID

python ../../REA_with_CESM2/data_extractor/extract.py --realm atm --h_identifier h2 --variable LHFLX --preprocessing regional_average --project_path ../../REA_heat_wEU_JJA/ --experiment_identifiers $ID

python ../../REA_with_CESM2/data_extractor/extract.py --realm lnd --h_identifier h7 --variable SOILWATER_10CM --preprocessing regional_average --project_path ../../REA_heat_wEU_JJA/ --experiment_identifiers $ID

python ../../REA_with_CESM2/data_extractor/extract.py --realm atm --h_identifier h1 --variable pr --preprocessing regional_average_precip --project_path ../../REA_heat_wEU_JJA/ --experiment_identifiers $ID

python ../../REA_with_CESM2/data_extractor/extract.py --realm atm --h_identifier h1 --variable TREFHT --preprocessing regional_average_TREFHT --project_path ../../REA_heat_wEU_JJA/ --experiment_identifiers $ID

python ../../REA_with_CESM2/evaluate_ensemble.py --project_path ../../REA_heat_wEU_JJA/ --experiment_identifiers $ID