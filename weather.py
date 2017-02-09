from urllib.request import urlopen #Python 3's way of accessing urllib
import json
from textmyself import textmyself #calling upon function from other file
apiKey=''#Enter api Key from Dark Sky
Lat= ''#Enter your Latitude
Long=''#Enter your Longitude
f= urlopen("https://api.darksky.net/forecast/"+ apiKey +'/'+ Lat +','+ Long)

json_string = f.read()
parsed_json = json.loads(json_string)

#Current
temperature = parsed_json['currently']['temperature']#current Temperaure
summary = parsed_json['currently']['summary']#Condition in text, ie 'partly cloudy'
feelsLike= parsed_json['currently']['apparentTemperature']#What the temperature feels like
#Daily
mintemp= parsed_json['daily']['data'][0]['temperatureMin']#low for the day
maxtemp= parsed_json['daily']['data'][0]['temperatureMax']#high for the day
humidity=  parsed_json['daily']['data'][0]['humidity']# %of humidity
rainChance= parsed_json['daily']['data'][0]['precipProbability']#chance of rain


message =('Temp: '+str(temperature)+" F"+
      '\nFeels Like: '+str(feelsLike)+" F"+
      '\nCurrently '+str(summary)+
      '\nHigh: '+str(maxtemp)+' F'+
      '\nLow: '+str(mintemp)+' F'+
      '\nRain: '+str(rainChance*100)+'%'+
      '\nHumidity: '+str(humidity*100)+'%')

textmyself(message)#sending the text

