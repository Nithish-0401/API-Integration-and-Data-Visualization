import json 
import requests
import matplotlib.pyplot as plt
#TO GET CITY NAME
city_name=input('Enter a City Name:') 
api_key='your api key'
# TO GET API URL
api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric' 
info=requests.get(api_url) 
json_data=info.json()
# converting into readable format
data=json.dumps(json_data,indent=4)
print(data)
temperature = json_data['main']['temp']
humidity = json_data['main']['humidity']
weather_description = json_data['weather'][0]['description']
pressure=json_data["main"]["pressure"]
wind=json_data["wind"]["speed"]
print("Temperature:",temperature,"°C")
print("Humidity:",humidity,"%")
print("Weather:",weather_description)
print("pressure:",pressure,"hPa")
print("wind speed:",wind,"m/s")
# Visualization
x=["wind(m/s)","Temperatue(°C)","Humditity(%)","Pressure(hPa)"]
y=[wind,temperature,humidity,pressure]
plt.bar(x,y,color=['blue','green','orange','cyan'])
plt.title("Weather Report")
plt.ylabel("Values")
plt.show()
