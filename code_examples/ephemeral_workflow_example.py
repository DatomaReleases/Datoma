# Make the necessary imports
from datoma import DatomaWorkflow

# Create an ephemeral DatomaWorkflow object
dw = DatomaWorkflow(path_yaml="path/to/yaml/file.yml", path_json="path/to/json/file.json")

# Set the global input
dw.set_global_input({"my_global_input": ["/path/to/folder/tims.d/"]}, True)

# modify the global parameter's value
dw.set_global_params({"my_global_param": True})

# Create a dictionary with the input files for the third step
input_dict = {"samples": ["path/to/file.mzML"]}

# Specify the step to which you want to set the input
dw.set_input('my_third_step', input_dict)

# Create a dictionary with parameters to modify from default values
params_dict = {'do_group_features': False, 
               'prefilter_n': 4}

# Set parameters of the job you want to modify
dw.set_params('my_third_step', params_dict)

# Submit the workflow to Datoma's infrastructure, you can name it if you want
dw.submit(name = "custom_workflow_execution")

# Check the status of the workflow, when it finishes, the output files will be downloaded
await dw.download(output_path="path/to/output/folder")

# Check the status of the workflow, when it finishes, the output files will be listed
print(await dw.list_outputs(regex=".*\.pkmat"))

# Printing the running time of the workflow (in seconds)
running_time = dw.finished_at - dw.running_at
print(running_time)