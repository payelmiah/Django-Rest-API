import requests
import json

URL = "http://127.0.0.1:8000/aicreate/"

# data to be sent to api 
data = {
    'id': 2,  # delete the record with id=1
}

json_data = json.dumps(data)
response = requests.delete(url = URL, data = json_data)
data = response.json()
print(data)
# Output: {'message': 'Record deleted successfully!'}