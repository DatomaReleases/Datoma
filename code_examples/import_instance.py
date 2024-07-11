# Make the necessary imports
from datoma import DatomaJob
from datoma import DatomaWorkflow

# Create objects from saved JSON files
job = DatomaJob(import_json = "path/to/file.json")
dw = DatomaWorkflow(import_json = "path/to/file.json")

# You can use the objects as usual
