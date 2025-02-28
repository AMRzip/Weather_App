Here's a comprehensive README.md for your weather app that explains how it works and how to set it up:

# Weather Comparison App

A modern Django web application that allows users to compare weather conditions and forecasts between two cities using OpenWeatherMap API.


![image](https://github.com/user-attachments/assets/706c1755-e32e-4b44-b3a8-7ee00b35a40c)


## Features

- Compare weather data between two cities side-by-side
- Display current weather conditions (temperature, description, icon)
- Show 5-day forecast for each selected city
- Modern, responsive dark-themed UI
- Clean visualization of weather data

## Technologies Used

- Python 3.10+
- Django 5.1.6
- OpenWeatherMap API
- HTML5/CSS3

## Installation

### Prerequisites

- Python 3.10 or higher
- OpenWeatherMap API key (sign up at [openweathermap.org](https://openweathermap.org/api))

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Weather-app.git
   cd Weather-app
   ```

2. Create and activate a virtual environment:
   ```bash
   # On Windows
   python -m venv WeatherApp
   WeatherApp\Scripts\activate

   # On macOS/Linux
   python -m venv WeatherApp
   source WeatherApp/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root:
   ```
   WEATHER_API=your_openweathermap_api_key_here
   HISTORY_API=your_openweathermap_history_api_key_here
   ```

5. Navigate to the Django project:
   ```bash
   cd WeatherApp/WeatherMain
   ```

6. Run migrations:
   ```bash
   python manage.py migrate
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

## Usage

1. Enter the name of the first city in the "Enter first city..." field
2. Optionally, enter a second city for comparison
3. Click the "Compare" button
4. View the current weather and 5-day forecast for both cities side-by-side

## Project Structure

```
Weather-app/
├── WeatherApp/                  # Virtual environment
├── WeatherMain/                 # Django project
│   ├── WeatherMain/             # Main project configuration
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py          # Django settings
│   │   ├── urls.py              # URL configuration
│   │   └── wsgi.py
│   └── main/                    # Main Django app
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── tests.py
│       ├── urls.py              # App URL configuration
│       ├── views.py             # View functions
│       └── templates/           # HTML templates
│           └── main/
│               ├── index.html   # Main comparison page
│               └── city.html    # City weather template
└── .env                         # Environment variables (API keys)
```

## API Usage

This app uses the following OpenWeatherMap API endpoints:

- Current weather data: `https://pro.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}`
- Historical data: `https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&appid={api_key}`

## Troubleshooting

- If you encounter a `TemplateDoesNotExist` error, make sure the `main/templates/main/` directory structure is correctly set up.
- If you see API key errors, verify your keys in the `.env` file and check if they're properly loaded in the application.
- For any other issues, check the Django development server logs for detailed error messages.

## Future Improvements

- Add user accounts to save favorite cities
- Implement more detailed weather information
- Add graphs for temperature trends
- Include air quality data
- Add weather alerts and notifications

## License

This project is licensed under the MIT License - see the LICENSE file for details.
