from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging
import requests

logging.basicConfig(level=logging.CRITICAL)

chatbot = ChatBot('MyTest')

conv = open('chats.txt','r').readlines()

trainer= ListTrainer(chatbot)

trainer.train(conv)

api_address='https://api.openweathermap.org/data/2.5/weather?appid=49a661c39797869a3bdd27dbe5b2263c&q='

      
while True:
    request = input ('Me :')

    if ('weather' in request):
        cityName= 'Mumbai'
        url = api_address  + cityName
        json_data = requests.get(url).json()
        formatted_data = json_data['weather'][0]['description']
        response ='Todays Weather is ' + formatted_data
        print(response)
    elif ('temperature' in request):
        cityName= 'Mumbai'
        url = api_address  + cityName
        json_data = requests.get(url).json()
        formatted_data = json_data['main'] 
        response = 'Maximum temperature is ' + str(formatted_data['temp_max']) + ' Minimum temperature is ' + str(formatted_data['temp_min'])
        print(response)
    elif ('bye' in request):
         print('MyBot:', 'Bye Bye.. Take Care')
         break
    else:       
        response= chatbot.get_response(request)
        print('MyBot:', response)



