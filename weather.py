import requests

location = input()

api_locate = "https://api.openweathermap.org/data/2.5/weather?q=" +location+"&appid="+'f342e6869478422df112c0d18000ffc1'
api_link = requests.get(api_locate)
api_data = api_link.json()


def weatherreport():
        if api_data['cod'] == '404':
           return f"Invalid City: {location}, Please check your City name."

        else:
            temp_city = ((api_data['main']['temp'])-273.15)
            weather_re = api_data['weather'][0]['description']

            return f"Current temprature of {location} is {temp_city} degree Celsius and the Current weather is {weather_re}"

