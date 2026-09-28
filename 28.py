import requests


def get_coordinates(city):
    """City name se latitude aur longitude nikalta hai."""

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, params=params, timeout=10)

    response.raise_for_status()

    data = response.json()

    if "results" not in data or len(data["results"]) == 0:
        return None

    result = data["results"][0]

    return {
        "name": result["name"],
        "country": result.get("country", ""),
        "latitude": result["latitude"],
        "longitude": result["longitude"]
    }


def get_weather(latitude, longitude):
    """Latitude aur longitude se current weather nikalta hai."""

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "auto"
    }

    response = requests.get(url, params=params, timeout=10)

    response.raise_for_status()

    return response.json()


def main():

    print("=" * 40)
    print("       WEATHER DATA CLI")
    print("=" * 40)

    city = input("Enter city name: ").strip()

    if not city:
        print("Please enter a city name.")
        return

    try:

        # Step 1: City -> Coordinates
        location = get_coordinates(city)

        if location is None:
            print("City not found.")
            return

        # Step 2: Coordinates -> Weather
        weather = get_weather(
            location["latitude"],
            location["longitude"]
        )

        current = weather["current"]

        print("\n" + "=" * 40)
        print("WEATHER INFORMATION")
        print("=" * 40)

        print("City       :", location["name"])
        print("Country    :", location["country"])
        print("Temperature:", current["temperature_2m"], "°C")
        print("Humidity   :", current["relative_humidity_2m"], "%")
        print("Wind Speed :", current["wind_speed_10m"], "km/h")

        print("=" * 40)

    except requests.exceptions.Timeout:
        print("Error: API request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Check your internet connection.")

    except requests.exceptions.HTTPError:
        print("Error: API returned an HTTP error.")

    except requests.exceptions.RequestException as e:
        print("API Error:", e)

    except KeyError:
        print("Error: Unexpected data received from API.")

    except Exception as e:
        print("Something went wrong:", e)


if __name__ == "__main__":
    main()