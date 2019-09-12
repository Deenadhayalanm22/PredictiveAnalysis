import requests

years_exp = {"yearsOfExperience": 8}

response = requests.post("{}/predict".format(), json = years_exp)

response.json()