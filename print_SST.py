
# This script prints the SST variable for a .nc file
import netCDF4 as nc

def extract_sst(nc_file_path):
    # Open the NetCDF file
    with nc.Dataset(nc_file_path, 'r') as ds:
        # Check if 'SST' variable exists in the file
        if 'SST' in ds.variables:
            # Extract the Sea Surface Temperature variable
            sst_variable = ds.variables['SST'][:]

            
            return sst_variable
        else:
            print("Error: 'SST' variable not found in the NetCDF file.")
            return None

# Varriables
file_path = 'met_em.d01.2012-10-27_07:00:00.nc'
sst_data = extract_sst(file_path)

if sst_data is not None:
    print("Sea Surface Temperature data extracted successfully.")
    print("Shape of SST data:", sst_data.shape)

