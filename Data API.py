import requests
import time
import json

url = "https://randomuser.me/api/"

while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
          
            user_data = response.json()['results'][0]
            print(json.dumps(user_data))
        time.sleep(2)
    except Exception as e:
        pass
