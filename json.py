import json
import requests

response = requests.get('http://api.opencorporates.com/companies/gb/00041424')
info = json.loads(response.text)
print info