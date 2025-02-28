from django.shortcuts import render
import datetime
import requests
from dotenv import dotenv_values

def index(request):
    env_vars = dotenv_values(".env")
    API_KEY = env_vars.get("WEATHER_API")
    HISTORY_API = env_vars.get('HISTORY_API')
    current_weather_url = "https://pro.openweathermap.org/data/2.5/weather?q={}&appid={}"
    forecast_url = "https://history.openweathermap.org/data/2.5/history/city?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}"

    if request.method == "POST":
        city1 = request.POST['city1']
        city2 = request.POST.get('city2', None)

        weather_data1, daily_forecast1 = fetch_weather_and_forecast(city1, API_KEY, HISTORY_API, current_weather_url, forecast_url)

        if city2:
            weather_data2, daily_forecast2 = fetch_weather_and_forecast(city2, API_KEY, HISTORY_API, current_weather_url, forecast_url)
        else:
            weather_data2, daily_forecast2 = None, None

        context = {
            "weather_data1": weather_data1,
            "daily_forecast1": daily_forecast1,
            "weather_data2": weather_data2,
            "daily_forecast2": daily_forecast2
        }

        return render(request, "main/index.html", context)

    else:
        return render(request, "main/index.html")

def fetch_weather_and_forecast(city, api_key, history_api, current_weather_url, forecast_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    # print(response)
    lat, lon = response['coord']['lat'], response['coord']['lon']
    forward_response = requests.get(forecast_url.format(lat, lon, history_api)).json()
    weather_data = {
        "city": city,
        "temperature": round(response['main']['temp'] - 273.15, 2),
        "description": response["weather"][0]['description'],
        "icon": response["weather"][0]['icon']
    }

    daily_forecasts = []
    for daily_data in forward_response['list'][:5]:
        daily_forecasts.append(
            {
                "day": datetime.datetime.fromtimestamp(daily_data['dt']).strftime("%A"),
                "min_temp": round(daily_data['main']['temp_min'] - 273.15, 2),
                "max_temp": round(daily_data['main']['temp_max'] - 273.15, 2),
                "description": daily_data["weather"][0]['description'],
                "icon": daily_data['weather'][0]['icon']
            }
        )

    return weather_data, daily_forecasts