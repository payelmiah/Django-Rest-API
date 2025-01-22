import requests
import json

URL = "http://127.0.0.1:8000/aicreate/" # request url

data = {
    'id': 3,
    "teacher_name": "Lam",
    "course_douration": 4,
}

json_data = json.dumps(data) #json.dumps() convert dictionary to json

response = requests.put(url = URL, data = json_data) # put request
data = response.json() # response to json extract
print(data) # print response