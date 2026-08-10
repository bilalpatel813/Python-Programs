import requests , os
from dotenv import load_dotenv
load_dotenv(".env")
API_KEY = os.getenv("API_KEY")
CITY ="Mumbai" # for default 

def get_weather(CITY,API_KEY):
    CITY = input("enter you city :").lower()
    url = "https://api.openweathermap.org/data/2.5/weather"
    params ={
        "q":CITY,
        "appid":API_KEY,
        "units":"metric" 
    }
    
    response = requests.get(url,params=params,timeout=5)
    if response.status_code == 200:
        data = response.json()
        c = data["main"]["temp"]
        f = (c * 9/5) + 32
        print("\nCity:", data["name"])
        print("Temperature:",c, "°C and ",f,"F" )
        print("Feels Like:", data["main"]["feels_like"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather Description :", data["weather"][0]["description"])
        print("Wind Speed:", data["wind"]["speed"], "m/s\n")
                
    else:
         print(response.json())
         
def main():
    while True:
        try:
            if CITY:
               get_weather(CITY,API_KEY)
            else:
               print("\nplease enter your city for weather report")
            user_input = input("do you want a weather report again ? (yes/no) :")
            if user_input == "yes" or user_input == "y":
               get_weather(CITY,API_KEY)
            elif user_input == "no" or user_input=="n":
               print("\ncome back again...")
               break    
        
        except  requests.exceptions.Timeout:
          print("\nRequest timed out.")
        except requests.exceptions.ConnectionError:
          print("\nno network connections")

if __name__ == '__main__':
    main()