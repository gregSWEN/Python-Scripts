import requests 

API_KEY = "4f4d0a95f3131789cb559719ff87d5bd"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def k_to_f(k):
    return ((k - 273.15) * (9/5)) + 32



def format(data):
    city = data["name"] #City name
    temp = round(k_to_f(data["main"]["temp"]), 2)
    kelvin_real = data['main']['feels_like']
    real_feel = round(k_to_f(kelvin_real), 2)
    max_temp = round(k_to_f(data["main"]["temp_max"]), 2)
    min_temp = round(k_to_f(data["main"]["temp_min"]), 2)
    description = data['weather'][0]["description"] #Description

    string = f"For today in {city}, the tempurature is {temp}F with a real feel of {real_feel}F. You can expect {description}s with a high of {max_temp}F and a low of {min_temp}F."

    return string

def main():
    while(True):
        city = input("Enter a city name or 'q' to quit: ")
        if(city.lower() == 'q'):
            print("We're sad to see you go...")
            break;
        request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
        response = requests.get(request_url)

        if response.status_code == 200:
            data = response.json()
            print(format(data))
        else: 
            code = response.status_code
            print(f"{code} error occured.")


if __name__ == "__main__":
    main()