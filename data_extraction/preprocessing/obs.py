import sys,glob
import xarray as xr
import numpy as np
sys.path.append('../../')
from experiment_configuration.main_observable import create_or_load_regional_mask, shift_lon, regional_average

name_addition = ''
preprocessing_attr = 'regional average over region of interest'

def preprocessor(archive_path, **kwargs):

    if 'initial_year' in kwargs.keys():
        search_path = f"{archive_path}/{kwargs['realm']}/hist/*{kwargs['h_identifier']}.{kwargs['initial_year']}*.nc"
    else:
        search_path = f"{archive_path}/{kwargs['realm']}/hist/*{kwargs['h_identifier']}*.nc"

    h_files = glob.glob(search_path)
    
    if len(h_files) == 1:
        nc = xr.open_dataset(h_files[0])
    
    elif len(h_files) > 1:
        nc = xr.open_mfdataset(h_files, combine='nested', concat_dim='time', data_vars='all')

    else:
        assert False, "h_file not found"

    # regional mask
    regional_mask = create_or_load_regional_mask(
        regional_mask_file = f"/work/bb1152/u290372/GKLT/regions/wEU.nc",
        slice_lat=slice(44,55), 
        slice_lon=slice(-4,12),
        )

    nc = shift_lon(nc)
    x = regional_average(nc['TREFHT'], regional_mask)
    x -= 273.15
    return xr.Dataset({'obs':x})
