import requests


url = "http://127.0.0.1:8000/api/auth/"
response = requests.post(url, data ={'username':'gigantic',
                                     'password':'gigantic'})
print(response.text)