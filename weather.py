import requests
import json

def weather():
  appid='9a0e4ffe23b84856975e1e4a72d739bb'
  city_id = 1508291
  res_now = requests.get(f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&units=metric&lang=ru&appid={appid}")
	#http://api.openweathermap.org/data/2.5/weather?id=1508291&units=metric&lang=ru&appid=9a0e4ffe23b84856975e1e4a72d739bb
  data_now = res_now.json()
  arr_now = [
  data_now['weather'][0]['description'], 
	data_now['main']['temp'],
	data_now['weather'][0]['icon']
	   ]
  F_CONST = 9/5
  fahr = int(arr_now[1])*F_CONST+32





  res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})	
  data = res.json()
 # print(arr_now)
  #print(data)
  arr_next = data['list'][13] # tommorow midday
  #print(type(arr_next)) #<- dict
  temp_next = arr_next['main']['temp']
  descr_next = arr_next['weather'][0]['description']
  wind_next = arr_next['wind']['speed']
  string_next = f'{round(temp_next)}\n{descr_next}\n{round(wind_next)}'
  print(string_next)
  #print(arr_next)


if __name__ == '__main__':  
  weather()