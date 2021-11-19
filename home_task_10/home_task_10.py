import requests

response = requests.get('https://httpbin.org/ip').json()
print(f'Your IP is {response["origin"]}')


