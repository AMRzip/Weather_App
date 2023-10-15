import requests
import json
import win32com.client as wincom
import time
import speech_recognition as sr
import pyaudio

def TTS(day, condition, temp, feels_temp):
    speak = wincom.Dispatch("SAPI.SpVoice")
    text = f"Good{day}"
    speak.Speak(text)
    time.sleep(1)

    text1 = f"Todays Weather consists of {condition} skies with Actual Temperature of {temp}, but it feels like {feels_temp}"
    speak.Speak(text1)
    time.sleep(1)

    text2 = "Hope you have a great day ahead"
    speak.Speak(text2)

def MicroInput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        city = r.recognize_google(audio, language='en-in')
        print(f"Selected city: {city}\n") 
    except Exception as e:
        print("Say that again please...") 
        return "None"
    return city

def GetWeather():
    city = MicroInput().lower
    api_key = "c858a7a32aba4e299dd182249231410"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key} &q={city}&aqi=no"
    response = requests.get(url)
    data = json.loads(response.text)
    day = data["current"]["is_day"]
    if day == 0:
        day = "Evening"
    elif day == 1:
        day = "Morning"
    print(day)
    condition = data["current"]["condition"]["text"]
    print(condition)
    temp = data["current"]["temp_c"]
    print(temp)
    feels_temp = data["current"]["feelslike_c"]
    print(feels_temp)
    TTS(day, condition, temp, feels_temp)

GetWeather()