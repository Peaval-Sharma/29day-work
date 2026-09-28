# 🌤️ Weather Data CLI

A simple **Python command-line weather application** that uses the **Open-Meteo API** to find a city's coordinates and display its current weather information.

The program takes a city name from the user, converts it into **latitude and longitude**, and then retrieves the current **temperature, humidity, and wind speed**.

## 📌 Features

* 🌍 Search weather by city name
* 📍 Get latitude and longitude automatically
* 🌡️ Display current temperature
* 💧 Display relative humidity
* 💨 Display wind speed
* 🌐 Automatically detect the city's timezone
* ⚠️ Handles API and network errors
* 🛡️ Uses exception handling for unexpected problems
* 💻 Simple command-line interface

## 🛠️ Technologies Used

* **Python**
* **Requests Library**
* **Open-Meteo Geocoding API**
* **Open-Meteo Weather API**

## 📂 Project Structure

```text
Weather-Data-CLI/
│
├── weather.py
└── README.md
```

## 📦 Installation

Make sure Python is installed on your system.

Install the `requests` library using:

```bash
pip install requests
```

If you are using Python 3:

```bash
python -m pip install requests
```

## ▶️ How to Run

Open the project folder in VS Code or terminal and run:

```bash
python weather.py
```

The program will ask:

```text
Enter city name:
```

Enter a city name, for example:

```text
Agra
```

## 💻 Example Output

```text
========================================
       WEATHER DATA CLI
========================================
Enter city name: Agra

========================================
WEATHER INFORMATION
========================================
City       : Agra
Country    : India
Temperature: 30.5 °C
Humidity   : 45 %
Wind Speed : 12.4 km/h
========================================
```

> Weather values change according to the current API data.

## 🔄 How It Works

The project works in two main steps:

### Step 1: City → Coordinates

The program sends the city name to the Open-Meteo Geocoding API.

It gets:

* City name
* Country
* Latitude
* Longitude

Example:

```text
Agra → Latitude + Longitude
```

### Step 2: Coordinates → Weather

The latitude and longitude are sent to the Open-Meteo Weather API.

The program retrieves:

* Temperature
* Relative humidity
* Wind speed

## 🌐 APIs Used

### Open-Meteo Geocoding API

Used to convert a city name into geographical coordinates.

```text
https://geocoding-api.open-meteo.com/v1/search
```

### Open-Meteo Weather API

Used to retrieve current weather information.

```text
https://api.open-meteo.com/v1/forecast
```

## 🧩 Python Concepts Used

This project helps practice several important Python concepts:

* Functions
* Dictionaries
* API requests
* JSON data
* `requests.get()`
* Query parameters
* Exception handling
* `try-except`
* `if-else`
* User input
* String formatting
* `.strip()`
* `.get()`
* `raise_for_status()`

## ⚠️ Error Handling

The program handles different types of errors:

### Timeout Error

```python
except requests.exceptions.Timeout:
```

Handles situations where the API takes too long to respond.

### Connection Error

```python
except requests.exceptions.ConnectionError:
```

Handles internet connection problems.

### HTTP Error

```python
except requests.exceptions.HTTPError:
```

Handles HTTP/API errors.

### Request Exception

```python
except requests.exceptions.RequestException:
```

Handles other request-related errors.

### Key Error

```python
except KeyError:
```

Handles unexpected API response data.

## 🚀 Future Improvements

Some possible improvements for this project are:

* Add weather condition descriptions
* Add weather icons/emojis
* Show today's forecast
* Show a 7-day forecast
* Add multiple city searches
* Add Celsius/Fahrenheit conversion
* Save weather results to a CSV file
* Create a graphical user interface
* Add a weather history feature

## 📚 Learning Outcome

After completing this project, you can understand how to:

1. Work with external APIs in Python.
2. Send GET requests using the `requests` library.
3. Pass parameters to an API.
4. Convert JSON responses into Python data.
5. Extract required information from dictionaries.
6. Handle API and network errors.
7. Build a practical command-line application.

## 👨‍💻 Author

**Praval**

Python Beginner Project — Weather Data CLI

## 📄 License

This project is created for **learning and educational purposes**.
