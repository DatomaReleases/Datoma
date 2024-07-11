# Make the necessary imports
from datoma import DatomaWorkflow

# Create a DatomaWorkflow object
dw = DatomaWorkflow(official_name = 'rmsiannotation')

# Create a dictionary with parameters to modify from default values
params_dict = {'preprocessing:smoothing:enable': False, 
               'preprocessing:smoothing:kernelsize': 8, 
               'preprocessing:alignment:bilinear': True, 
               'preprocessing:alignment:maxShiftppm': 20}

# Set parameters of the job you want to modify
dw.set_params('rmsi2', params_dict)

# Create a dictionary with input data, specifying key and value(s)
global_input_dict = {"imaging_files":[{"file":"/path/to/file.ibd"},
                                      {"file":"/path/to/file.imzML"}]}

# Set the global input of the workflow
dw.set_global_input(global_input_dict, preserve_name = True)

# Submit the workflow to Datoma's infrastructure, you can name it if you want
dw.submit(name = "rmsiannotation_execution")

# Check the status of the workflow, when it finishes, the output files will be downloaded
await dw.download(output_path="path/to/output/folder")

# Check the status of the workflow, when it finishes, the output files will be listed
print(await dw.list_outputs(regex=".*\.imzML"))