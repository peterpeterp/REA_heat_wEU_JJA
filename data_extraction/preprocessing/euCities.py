import sys,glob
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

    l = []
    for y, x, name in [
        # Western Europe
        (52.5200, 13.4050, "Berlin"),        # Germany
        (48.8566, 2.3522, "Paris"),          # France
        (51.5074, -0.1278, "London"),        # UK
        (52.3676, 4.9041, "Amsterdam"),      # Netherlands
        (50.8503, 4.3517, "Brussels"),       # Belgium

        # Northern Europe
        (59.3293, 18.0686, "Stockholm"),     # Sweden
        (60.1699, 24.9384, "Helsinki"),      # Finland
        (55.6761, 12.5683, "Copenhagen"),    # Denmark
        (64.1466, -21.9426, "Reykjavik"),    # Iceland

        # Southern Europe
        (40.4168, -3.7038, "Madrid"),        # Spain
        (41.9028, 12.4964, "Rome"),          # Italy
        (37.9838, 23.7275, "Athens"),        # Greece
        (38.7223, -9.1393, "Lisbon"),        # Portugal

        # Eastern Europe
        (55.7558, 37.6173, "Moscow"),        # Russia
        (50.0647, 19.9450, "Krakow"),        # Poland
        (47.4979, 19.0402, "Budapest"),      # Hungary
        (44.4268, 26.1025, "Bucharest"),     # Romania
        (50.4501, 30.5234, "Kyiv"),          # Ukraine
        (42.6977, 23.3219, "Sofia")          # Bulgaria
    ]:
        xxx = nc.sel(dict(lat=y, lon=x), method='nearest').squeeze()
        xxx = xxx.expand_dims('city')
        xxx = xxx.assign_coords(city=[name])
        l.append(xxx)

    return xr.concat(l, dim='city')