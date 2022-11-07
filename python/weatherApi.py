import json
import requests

print('Please enter your zip code:')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=4ef07cd35781e390660e28cf8a1b9f4b' % zip)
data=r.json()
print(data['weather'][0]['description'])