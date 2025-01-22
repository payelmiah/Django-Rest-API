import requests

URL = "http://127.0.0.1:8000/aiquest/" # request url

response = requests.get(url=URL) # get request
data = response.json() # get json data
print(data)