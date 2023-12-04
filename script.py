import os
from netCDF4 import Dataset

def replace_sst_variable(input_folder, output_folder, date_to_replace):
    # Form the input and output file paths
    file_2012 = f"met_em.d01.2012-{date_to_replace}.nc"
    path_2012 = os.path.join(input_folder, file_2012)

    file_2022 = f"met_em.d01.2022-{date_to_replace}.nc"
    path_2022 = os.path.join(input_folder, file_2022)

    output_path = os.path.join(output_folder, file_2022)

    # Open the NetCDF files for 2012 and 2022
    with Dataset(path_2012, 'r') as ds_2012, Dataset(path_2022, 'r') as ds_2022:
        # Extract the sea surface temperature variable from 2012
        sst_2012 = ds_2012.variables['SST'][:]

        # Open the 2022 file in write mode to modify it
        with Dataset(output_path, 'w') as ds_out:
            # Copy attributes and dimensions from 2022 to the output file

            for name, dimension in ds_2022.dimensions.items():
                ds_out.createDimension(name, len(dimension) if not dimension.isunlimited() else None)

            for name, variable in ds_2022.variables.items():
                out_var = ds_out.createVariable(name, variable.datatype, variable.dimensions)
                out_var.setncatts({k: variable.getncattr(k) for k in variable.ncattrs()})
                if name == 'SST':
                    # Replace the sea surface temperature variable values 
with 2012 values
                    out_var[:] = sst_2012
                else:
                    # Copy other variables as is
                    out_var[:] = variable[:]

    print(f"Replacement for {file_2022} completed successfully!")

# Get a list of all .nc files in the current directory

current_directory = os.getcwd()

nc_files = [f for f in os.listdir(current_directory) if f.endswith('.nc')]

# Iterate through the list of files and perform the replacement

for nc_file in nc_files:
    date_to_replace = nc_file[11:29]  # Adjust the index based on your  actual file naming convention
    replace_sst_variable(current_directory, current_directory, date_to_replace)

