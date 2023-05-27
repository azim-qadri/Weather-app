```
# Python Tkinter Weather Application

This is a simple weather application built with Python Tkinter that allows users to fetch weather information using the OpenWeather API. The application prompts users to enter either a zip code or a location to retrieve the current weather conditions.

## Features

- Fetches weather information using the OpenWeather API
- Supports weather retrieval based on zip code or location
- Displays current weather conditions including temperature, humidity, wind speed, and description

## Prerequisites

- Python 3.x
- Tkinter (usually bundled with Python)

## Installation

1. Clone the repository:

```shell
git clone https://github.com/azim-qadri/weather-app.git
```

2. Navigate to the project directory:

```shell
cd weather-app
```

3. Install the required dependencies:

```shell
pip install -r requirements.txt
```

## Usage

1. Run the application:

```shell
python weather_app.py
```

2. Enter the zip code or location in the provided input field.
3. Click the "Fetch Weather" button.
4. The current weather information will be displayed in the application window.

## Configuration

The application uses the OpenWeather API to fetch weather data. To use the API, you need to obtain an API key. Follow these steps to configure the API key:

1. Go to the [OpenWeatherMap website](https://openweathermap.org/) and sign up for an account.
2. Once signed in, navigate to your account dashboard and find the API Keys section.
3. Generate a new API key if you don't have one already.
4. Open the `weather_app.py` file in a text editor.
5. Locate the following line of code:

```python
API_KEY = "YOUR_API_KEY"
```

6. Replace `YOUR_API_KEY` with your actual OpenWeather API key.
7. Save the changes.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute, suggest improvements, or report issues. Any feedback is appreciated!

```
