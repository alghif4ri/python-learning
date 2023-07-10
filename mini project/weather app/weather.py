import requests

city = input("Enter your city : ")

api_key = "b435a4ac911e441daba71834231007"
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    temperature = data['current']['temp_c']
    condition = data['current']['condition']['text']
    humidity = data['current']['humidity']

    print(f"Temperature: {temperature}°C")
    print(f"Condition: {condition}")
    print(f"Humidity: {humidity}")
else:
    print("Error")
print(data)
