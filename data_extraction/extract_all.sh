#!/bin/bash

cd ../../REA_with_CESM2/data_extractor

ID=$1

python ../../REA_with_CESM2/data_extractor/extract.py --realm atm --h_identifier h1 --variable TREFHT --project_path ../../REA_heat_wEU_JJA/ --experiment_identifiers $ID --preprocessing euCities --overwrite

python ../../REA_with_CESM2/data_extractor/extract.py --realm atm --h_identifier h1 --variable pr --preprocessing euCities_pr --project_path ../../REA_heat_wEU_JJA/ --experiment_identifiers $ID --overwrite

python ../../REA_with_CESM2/data_extractor/extract.py --realm lnd --h_identifier h7 --variable SOILWATER_10CM --project_path ../../REA_heat_wEU_JJA/ --experiment_identifiers $ID --preprocessing euCities --overwrite



exit 0

python ../../REA_with_CESM2/data_extractor/extract.py --realm atm --h_identifier h2 --variable SHFLX --project_path ../../REA_heat_wEU_JJA/ --experiment_identifiers $ID --preprocessing euCities --overwrite

python ../../REA_with_CESM2/data_extractor/extract.py --realm atm --h_identifier h2 --variable LHFLX --project_path ../../REA_heat_wEU_JJA/ --experiment_identifiers $ID --preprocessing euCities --overwrite

exit 0



exit 0

python ../../REA_with_CESM2/data_extractor/extract.py --realm atm --h_identifier h1 --variable V500 --project_path ../../REA_heat_wEU_JJA/ --experiment_identifiers $ID


python ../../REA_with_CESM2/data_extractor/extract.py --realm atm --h_identifier h1 --variable TREFHT --preprocessing regional_average_TREFHT --project_path ../../REA_heat_wEU_JJA/ --experiment_identifiers $ID

python ../../REA_with_CESM2/data_extractor/extract.py --realm atm --h_identifier h1 --variable obs --preprocessing obs --project_path ../../REA_heat_wEU_JJA/ --experiment_identifiers $ID

python ../../REA_with_CESM2/evaluate_ensemble.py --project_path ../../REA_heat_wEU_JJA/ --experiment_identifiers $ID

python ../../REA_with_CESM2/data_extractor/extract.py --realm atm --h_identifier h2 --variable SHFLX --preprocessing regional_average --project_path ../../REA_heat_wEU_JJA/ --experiment_identifiers $ID

python ../../REA_with_CESM2/data_extractor/extract.py --realm atm --h_identifier h2 --variable LHFLX --preprocessing regional_average --project_path ../../REA_heat_wEU_JJA/ --experiment_identifiers $ID

python ../../REA_with_CESM2/data_extractor/extract.py --realm lnd --h_identifier h7 --variable SOILWATER_10CM --preprocessing regional_average --project_path ../../REA_heat_wEU_JJA/ --experiment_identifiers $ID

python ../../REA_with_CESM2/data_extractor/extract.py --realm atm --h_identifier h1 --variable pr --preprocessing regional_average_precip --project_path ../../REA_heat_wEU_JJA/ --experiment_identifiers $ID

