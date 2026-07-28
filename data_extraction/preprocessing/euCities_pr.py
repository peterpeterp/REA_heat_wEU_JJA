import sys,glob,pickle
import xarray as xr
import numpy as np

name_addition = '-euCities'
preprocessing_attr = 'some cities in Europe'


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

    with open('/home/u/u290372/projects/post_heat_wEU_JJA/a_cities/city_locations.pkl', 'rb') as fl:
        city_locations = pickle.load(fl)

    l = []
    for city_name in city_locations.keys():
        y,x = city_locations[city_name]
        xxx = nc.sel(dict(lat=y, lon=x), method='nearest').squeeze()
        xxx = xxx.expand_dims('city')
        xxx = xxx.assign_coords(city=[city_name])
        pr = xxx['PRECC'] + xxx['PRECL'] 
        pr *= 24*60*60 * 1000
        l.append(xr.Dataset({'pr':pr}))

    return xr.concat(l, dim='city')