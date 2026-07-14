import sys,glob
import xarray as xr
import numpy as np

name_addition = '-rbEU'
preprocessing_attr = 'big rectangle around Europe'

def preprocessor(archive_path, **kwargs):

    search_path = f"{archive_path}/{kwargs['realm']}/hist/*{kwargs['h_identifier']}*.nc"
    h_files = glob.glob(search_path)
    
    if len(h_files) == 1:
        nc = xr.open_dataset(h_files[0])
    
    elif len(h_files) > 1:
        nc = xr.open_mfdataset(h_files, combine='nested', concat_dim='time', data_vars='all')

    else:
        assert False, "h_file not found"

    nc = nc.roll(lon=144, roll_coords=True)
    nc = nc.assign_coords(lon=(nc.lon + 180) % 360 - 180).sel(dict(lat=slice(10,80), lon=slice(-30,50)))
    return nc