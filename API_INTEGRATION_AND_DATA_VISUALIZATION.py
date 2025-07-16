import requests
import matplotlib.pyplot as plt

city_name = input("Enter city name: ").strip().title()
API_KEY = "9fff63a0978a39e3507d4ab1d2cb333e" 
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()

    temp = data['main']['temp']
    humidity = data['main']['humidity']
    weather_desc = data['weather'][0]['description']

    print(f"\nCity: {city_name}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {weather_desc}")

    labels = ['Temperature (°C)', 'Humidity (%)']
    values = [temp, humidity]
    colors = ['orange', 'skyblue']
    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=colors)
    plt.title(f"Current Weather in {city_name}")
    plt.ylim(0, 100)
    plt.show()

else:
    print("Failed to fetch data. Please check the city name.")
