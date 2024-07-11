# Make the necessary imports
from datoma import DatomaJob

# Create a DatomaJob object
job = DatomaJob("xcms", "xcmspeakpicking")

# Create a dictionary with input data
input_dict = {"samples": ["path/to/file.mzML"]}

# Preserve file names when uploaded to Datoma (some tools require identical input file names)
job.set_input(input_dict, preserve_name = True)

# Create a dictionary with parameters to modify from default values
params_dict = {'do_group_features': False, 
               'prefilter_n': 4}
job.set_params(params_dict)

# Submit the job to Datoma's infrastructure, you can name the job if you want
job.submit(job_name = "xcms_execution")

# Check the status of the job, when it finishes, the output files will be downloaded
await job.download(output_path="path/to/output/folder")

# Check the status of the job, when it finishes, the output files will be listed
print(await job.list_outputs(regex=".*\.csv"))

# We export the job to a JSON file for later usage
job.export_json(path = "path/to/file.json")

# Printing the running time of the job (in seconds)
running_time = job.finished_at - job.running_at
print(running_time)