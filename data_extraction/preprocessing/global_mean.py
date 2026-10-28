import sys,glob
import xarray as xr
import numpy as np

name_addition = '-GM'
preprocessing_attr = 'global mean (lat weighted)'

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

    variable = kwargs['variable']
    x = nc[variable]
    x = x.weighted(np.cos(np.radians(x.lat))).mean(('lon','lat'))
    return xr.Dataset({variable:x})