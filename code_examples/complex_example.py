# Make the necessary imports
from datoma import DatomaJob
from datoma import DatomaWorkflow

# Create DatomaJob and DatomaWorkflow objects
job = DatomaJob("rmsistd", "rmsi")
dw = DatomaWorkflow(official_name = 'rmsiannotation')

# set the job's input
job.set_input(  input_dict = {"input": [
                            {"file":"path/to/file.ibd"}, 
                            {"roi":"path/to/file.imzML"}]}, 
                preserve_name = True)

# Create a dictionary with parameters to modify from the task's default values
job.set_params(params_dict =    {'preprocessing:smoothing:enable': False, 
                                'preprocessing:smoothing:kernelsize': 8})

# Submit the job to Datoma's infrastructure, you can name the job if you want
job.submit(job_name = "rmsi_execution")

# We will store the location of the "*.imzML" files in a variable
output_files, total_size = await job.list_outputs(regex=".*\.imzML")

# Get the total size of the filtered output files 
print(total_size)

# In this case, we are using job's output as input for the workflow
# The output files are located in Datoma's infrastructure 's3://...'
global_input_dict = {"imaging_files":[{"file":"/path/to/file.ibd"},
                                      {"file": output_files[0]}]}

# Set the global input of the workflow
dw.set_global_input(global_input_dict, preserve_name = True)

# Submit the workflow to Datoma's infrastructure, you can name it if you want
dw.submit(name = "rmsiannotation_execution")

# Check the status of the workflow, when it finishes, the output files will be downloaded
await dw.download(output_path="path/to/output/folder")

# You can also export the workflow to a json file
dw.export_json("path/to/save/file.json")