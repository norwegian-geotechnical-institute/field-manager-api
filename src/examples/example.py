from field_manager_api.field_manager import FieldManagerAPI


fm = FieldManagerAPI()
token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJQZGRrU2pfVGpwWEpQTnVXNjlkaEFkQTRiNE0xLVlJU24yMVRMQ2NRd24wIn0.eyJleHAiOjE3MjcwODExNDEsImlhdCI6MTcyNzA3Mzk0MSwiYXV0aF90aW1lIjoxNzI3MDczOTQxLCJqdGkiOiI5YmFhOWM0OC1mMGYzLTRkOTQtOThlNS1iYTRiZjRmYjAwNmIiLCJpc3MiOiJodHRwczovL2tleWNsb2FrLnRlc3QubmdpYXBpLm5vL2F1dGgvcmVhbG1zL3RlbmFudC1nZW9odWItcHVibGljIiwiYXVkIjpbIm5naWxpdmUtbGthYi1ncmFmYW5hdjIiLCJnZW9odWItY2xpZW50IiwiY29waXQtb2F1dGgtcHJveHkiLCJuZ2lsaXZlLW5naS1ncmFmYW5hdjIiLCJhY2NvdW50Il0sInN1YiI6IjhhMDk4MjYwLTRlMzUtNDNkMC04MzYzLWRkOWFlZjc1ZTJkZiIsInR5cCI6IkJlYXJlciIsImF6cCI6ImZpZWxkbWFuYWdlci1jbGllbnQiLCJub25jZSI6IjE2YTA1OWQzLTBmYTctNGM4OS04MGQ2LTQxZDI2OWI4ZTljNyIsInNlc3Npb25fc3RhdGUiOiI3ZmY0ZjhiZS1lNTA4LTRiMWYtOWQxYi1jNzZhOGVkZWZlYzUiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cHM6Ly9hcHAudGVzdC5maWVsZG1hbmFnZXIuaW8iLCJodHRwOi8vbG9jYWxob3N0Ojg1MDEiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbInRlbmFudC1nZW9odWItcHVibGljIiwicmVhbG0tY2xpZW50LWFkbWluIiwibmdpX25vcndheV9vcmciLCJkZWZhdWx0LXJvbGVzLXRlbmFudC1nZW9odWItcHVibGljIiwib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7Im5naWxpdmUtbGthYi1ncmFmYW5hdjIiOnsicm9sZXMiOlsiVmlld2VyIl19LCJnZW9odWItY2xpZW50Ijp7InJvbGVzIjpbInJlZmVyZW5jZSIsImVkaXRvciIsInZpZXdlciIsImFkbWluIl19LCJjb3BpdC1vYXV0aC1wcm94eSI6eyJyb2xlcyI6WyJjb3BpdC1hY2Nlc3MiXX0sIm5naWxpdmUtbmdpLWdyYWZhbmF2MiI6eyJyb2xlcyI6WyJWaWV3ZXIiXX0sImZpZWxkbWFuYWdlci1jbGllbnQiOnsicm9sZXMiOlsicmVmZXJlbmNlIiwiYWRtaW4tcHJvai1hOTM1ODI1Zi1hNGEwLTQwYjUtOTUxNS02ZWY0MzE5OTdlZjQiLCJ2aWV3ZXIiLCJyZWZlcmVuY2Utb3JnLTg3MDUyNWIyLThmMmItNGQyNC04YTEyLTBiZTc2NjYyOGZiMyIsImVkaXRvciIsInZpZXdlci1vcmctODcwNTI1YjItOGYyYi00ZDI0LThhMTItMGJlNzY2NjI4ZmIzIiwicmVmZXJlbmNlLW9yZy0zZWM0NGJlOC05ZTdjLTQyOTktYmZjMy0xMzdlMmMzMDViNDAiLCJyZWZlcmVuY2Utb3JnLTdhMzU2YmU2LWY3ZTItNDQzYi04MjU3LWJjOTAxNzNkN2JhZiIsImFkbWluIiwicmVmZXJlbmNlLXByb2otYTkzNTgyNWYtYTRhMC00MGI1LTk1MTUtNmVmNDMxOTk3ZWY0IiwiYWRtaW4tcHJvai0xNmViOTc0ZS0yYjFkLTRjZDEtYWFlMS03MzdjYWU5MzZlZTAiLCJyZWZlcmVuY2UtcHJvai0xNmViOTc0ZS0yYjFkLTRjZDEtYWFlMS03MzdjYWU5MzZlZTAiXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgcHJvamVjdDpyZWFkIG1hcC1vcmctY2xhaW0gZW1haWwiLCJzaWQiOiI3ZmY0ZjhiZS1lNTA4LTRiMWYtOWQxYi1jNzZhOGVkZWZlYzUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwib3JnIjoiODcwNTI1YjItOGYyYi00ZDI0LThhMTItMGJlNzY2NjI4ZmIzIiwibmFtZSI6IlRlbGxlZiBLeWRsYW5kIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidGVsbGVmLmt5ZGxhbmRAbmdpLm5vIiwiZ2l2ZW5fbmFtZSI6IlRlbGxlZiIsImZhbWlseV9uYW1lIjoiS3lkbGFuZCIsImVtYWlsIjoidGVsbGVmLmt5ZGxhbmRAbmdpLm5vIn0.C5VcEX5X2I4Xct6WXE7MhpLWMH2NXm9NrlS7I1UHj9oxXm3jcZJ4wl3LOyRWZz0kl17KXHJbNYfyyTIYuGN3Lbo2krl-9XaXTpkiqCkbqhOlVYTzXvl3qr1t4rJwYWVRSBmFj4rVo9gl7194x-ImbE7B2oTZBTZTc6tJPDWBPSNeGqvrxx-EQBYATL2madR63lSds-R5QRBPdJ94BKU-_lPAMgOa_RtWwjAFAI8WJc1KO0nDDuKCSvvP3GKKr0yc0NuKFdnArflAhHprAc1HrNYuczUEEd13cezJnaj-q8Aq9JkCt1kHs5TehAvjnPOhoCsfG4tjCr7y8awt3hgZlA"
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
