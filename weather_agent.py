import os
import requests
from typing import Dict, Any


def fetch_jma_forecast(area_code: str = "130000") -> Dict[str, Any]:
    """Fetch forecast data from Japan Meteorological Agency.

    Parameters
    ----------
    area_code: str
        The JMA area code. Defaults to Tokyo (130000).

    Returns
    -------
    dict
        Parsed JSON response from JMA.
    """
    url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def fetch_openweather(city: str = "Tokyo", country: str = "JP") -> Dict[str, Any]:
    """Fetch current weather from OpenWeatherMap.

    Requires the OPENWEATHER_API_KEY environment variable to be set.

    Parameters
    ----------
    city: str
        City name. Defaults to Tokyo.
    country: str
        Country code. Defaults to JP.

    Returns
    -------
    dict
        Parsed JSON response from OpenWeatherMap.
    """
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENWEATHER_API_KEY environment variable not set")

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city},{country}&units=metric&appid={api_key}"
    )
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def main():
    jma_data = fetch_jma_forecast()
    ow_data = fetch_openweather()

    print("JMA forecast (Tokyo):")
    print(jma_data[0]["timeSeries"][0]["areas"][0])

    print("\nOpenWeatherMap current weather (Tokyo):")
    print({
        "description": ow_data["weather"][0]["description"],
        "temperature": ow_data["main"]["temp"],
        "humidity": ow_data["main"]["humidity"],
    })


if __name__ == "__main__":
    main()
