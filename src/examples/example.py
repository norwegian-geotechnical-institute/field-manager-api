from field_manager_api.field_manager import FieldManagerAPI


fm = FieldManagerAPI()
# set token from https://app.test.fieldmanager.io/devloper
token = "your_token"
fm.set_token(token)
fm.get_projects()
fm.set_project(
    project_name="TellefTesterTing"
)  # /fm.set_project(project_id="e1a73be4-7269-4738-a1cb-1bb87b0e37c5")
fm.get_locations()
fm.get_methods()

fm.plot_locations()
fm.create_ground_model()
fm.plot_heatmap()
fm.create_bedrock_model()
fm.create_datarapport()
