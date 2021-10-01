import xarray as xr
import numpy as np
import pooch

import unpackqa

L8_QA_PIXEL_FILE = 'https://landsat.usgs.gov/sites/default/files/C2_Sample_Data/LC08_L1TP_140041_20130503_20200912_02_T1.zip'
L8_qa_product = 'LANDSAT_8_C2_L2_QAPixel'

file_path = pooch.retrieve(
    L8_QA_PIXEL_FILE,
    known_hash=None,
    processor=pooch.Unzip()
)

my_file = [f for f in file_path if 'QA_PIXEL' in f][0]
ds = xr.open_rasterio(my_file, chunks={'x':2000,'y':2000})

# Drop the band axis since the file has a single band.
ds = ds.isel(band=0)

#-------------------------------
# with unpack_to_array
# resulting in flags as an added dimension
L8_flag_names = unpackqa.list_qa_flags(L8_qa_product)

flag_ds = xr.apply_ufunc(
    unpackqa.unpack_to_array,
    ds,
    kwargs = dict(product=L8_qa_product),
    output_core_dims = [['flag']],
    dask_gufunc_kwargs = dict(output_sizes={'flag':len(L8_flag_names)}),
    output_dtypes=[np.uint8],
    vectorize=False,
    dask='parallelized'
    )

# put labels on the flag coordinates
flag_ds['flag'] = L8_flag_names

# execute all lazy computations and load full dataset into memory.
flag_ds.load()

# Another option would be to have each flag as it's own data variable.
# That can be done with some rearranging.
flag_ds2 = [flag_ds.sel(flag=flag_name).drop('flag').rename(flag_name) for flag_name in L8_flag_names]
flag_ds2 = xr.merge(flag_ds2)




