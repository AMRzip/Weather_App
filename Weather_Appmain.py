[1mdiff --git a/main.py b/main.py[m
[1mindex e69de29..5911dac 100644[m
[1m--- a/main.py[m
[1m+++ b/main.py[m
[36m@@ -0,0 +1,42 @@[m
[32m+[m[32mimport requests[m
[32m+[m[32mimport json[m
[32m+[m[32mimport win32com.client as wincom[m
[32m+[m[32mimport time[m
[32m+[m
[32m+[m[32mdef TTS(day, condition, temp, feels_temp):[m
[32m+[m[32m    speak = wincom.Dispatch("SAPI.SpVoice")[m
[32m+[m[32m    text = f"Good{day}"[m
[32m+[m[32m    speak.Speak(text)[m
[32m+[m[32m    time.sleep(1)[m
[32m+[m
[32m+[m[32m    text1 = f"Todays Weather consists of {condition} skies with Actual Temperature of {temp}, but it feels like {feels_temp}"[m
[32m+[m[32m    speak.Speak(text1)[m
[32m+[m[32m    time.sleep(1)[m
[32m+[m
[32m+[m[32m    text2 = "Hope you have a great day ahead"[m
[32m+[m[32m    speak.Speak(text2)[m
[32m+[m
[32m+[m
[32m+[m[32mdef GetWeather():[m
[32m+[m[32m    api_key = "c858a7a32aba4e299dd182249231410"[m
[32m+[m[32m    # city = input("Enter the name of City: ")[m
[32m+[m[32m    # city.lower()[m
[32m+[m[32m    city = "Jaipur"[m
[32m+[m[32m    url = f"http://api.weatherapi.com/v1/current.json?key={api_key} &q={city}&aqi=no"[m
[32m+[m[32m    response = requests.get(url)[m
[32m+[m[32m    data = json.loads(response.text)[m
[32m+[m[32m    day = data["current"]["is_day"][m
[32m+[m[32m    if day == 0:[m
[32m+[m[32m        day = "Evening"[m
[32m+[m[32m    elif day == 1:[m
[32m+[m[32m        day = "Morning"[m
[32m+[m[32m    print(day)[m
[32m+[m[32m    condition = data["current"]["condition"]["text"][m
[32m+[m[32m    print(condition)[m
[32m+[m[32m    temp = data["current"]["temp_c"][m
[32m+[m[32m    print(temp)[m
[32m+[m[32m    feels_temp = data["current"]["feelslike_c"][m
[32m+[m[32m    print(feels_temp)[m
[32m+[m[32m    TTS(day, condition, temp, feels_temp)[m
[32m+[m
[32m+[m[32mGetWeather()[m
\ No newline at end of file[m
