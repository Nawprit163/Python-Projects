"""
Hi! Welcome to Veera Voice Assistant. This application is going to help you with your daily tasks.
This application sends emails to diffrent users, you can listen to music, you can open spotify, open goggle,
open instagram,youtube. You can ask Veera the time, date, you can play game with Veera and you can also chat with it.
In this some features are avilable and some are still to be added, like Veera will be understanding the sentiments, emotions,
and on the basis of that it can reply you, it willl be telling you jokes for which i will be importing an API which will be useful
and many more yet to come...................
"""

# WELCOMING VEERA


import pyttsx3  # it is a text to speech module
import datetime
# this module is used to take input from user as a voice command
import speech_recognition as sr
import wikipedia
import webbrowser
import os  # this module is for basic opreating system operations to perform
import random  # this module genrates a random number,floating pt number, etc..... in a random way
import smtplib as s  # this module is used to provide the email functionalities
import requests
import json
import randfacts
from weather import *

# created a list of contacts whom you want to send emails
contacts = ["bobbysimon163@gmail.com",
            "Navpreetsaini2580@gmail.com", "unknown@gmail.com"]


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)


# creating a function audio which is going to speak and answer your queries through speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


today_date = datetime.datetime.now()
today=today_date.strftime("%B %d %Y")
# A function which is used to greet when you run the system


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak(f"Today is {today}")
    speak("I am Veera and I am your personal assistant and I am here to assist you. Tell me how can i help you today? ")


# This function takes microphone input from the user and returns string output

# if "how" and "about" and "you" in query:
#         speak("Thankyu for asking, I am having a good day!")
#         speak("Tell me how can I aid you today!")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")

        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Speak it again please...")
        return "None"
    return query


# This function is going to read top headlines using news.api

def newsRead():

    response = requests.get(
        'https://newsapi.org/v2/top-headlines?country=in&apiKey=397e2c44e0f042dabe63b9941f6a2421')
    data = json.loads(response.content)

    for i in range(3):
        news = data['articles'][i]['title']
        speak("Sure, I will read news for you!")
        speak("number"+str(i+1)+news+".")
        print("number"+str(i+1)+news+".")


# *********************************************************************************************************************
if __name__ == "__main__":
    print(__doc__)
    greet()
    while True:
        query = takeCommand().lower()

# logic for executing tasks based on query

# opening wikipedia

        if 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            print(results)
            speak("According to wikipedia")
            speak(results)

# opening youtube
        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")

# opening goggle
        elif 'open goggle' in query:
            webbrowser.open("goggle.com")

# opening spotify
        elif 'open spotify' in query:
            codePath = "Dekstop"
            os.startfile(codePath)
            # webbrowser.open("spotify.com")

# It will randomly play any music from the list of music in your playlist and here we use random module and os module to open the directory
        elif 'play music' in query:
            music_dir = 'E:\\BOBBY\\BOBBY EXTRA  STUFFS\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))


# date and time module is used to tell the time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%H:%S")
            speak(f"Right now the time is {strTime}")
            print(strTime)

# it will open VScode, we again used os module to get the path of the vscode
        elif 'open code' in query:
            codePath = "C:\\Users\\Nawprit Saini\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

# it will tell the temprature of a specific city all over the globe you want to know.you just have to input the location
        elif 'open weather' or 'tell weather' in query:
            speak("Which City's weather you want to know?")
            location = input()

            api_locate = "https://api.openweathermap.org/data/2.5/weather?q=" + \
                location+"&appid="+'f342e6869478422df112c0d18000ffc1'
            api_link = requests.get(api_locate)
            api_data = api_link.json()

            try:
                temp_city = ((api_data['main']['temp'])-273.1)
                weather_re = api_data['weather'][0]['description']

                speak(
                    f"Current temprature of {location} is {temp_city} degree Celsius and the Current weather is {weather_re}")

            except Exception as e:
                api_data['cod'] == '404'
                speak(
                    f"Invalid City: {location}, Please check your City name.")


# this is going to read news for you
        elif 'read news' in query:
            newsRead()

# for this i actually did'nt make any function, it is going to tell you a random fact
        elif 'fact' or 'facts' in query:
            x = randfacts.get_fact()
            print(x)
            speak(f"Did you know that {x}")
