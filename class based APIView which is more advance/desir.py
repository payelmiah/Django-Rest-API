import requests
import json

# data creation
URL = "http://127.0.0.1:8000/aicreate/"

#create dictionary
data = {
    "teacher_name": "Mejbah",
    "course_name": "Deep Learning",
    "course_douration": 3,
    "seat": 20
}

#convert dictionary to json
json_data = json.dumps(data) #json.dumps() convert dictionary to json

#post request
response = requests.post(url = URL, data = json_data)
data = response.json()
print(data)
