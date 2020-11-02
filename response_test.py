import requests

r = requests.get('https://www.pro-football-reference.com/years/2019/')
print(r.text)