import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

import requests
from bs4 import BeautifulSoup

def scrapeTemp():
    url = 'https://www.surf-forecast.com/breaks/Rossnowlagh/seatemp'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    temperature = soup.find('span', class_='temp').text
    # print(f"The water temperature at Rossnowlagh is: {temperature} degrees Celsius.")
    return temperature

def get_water_temperature():
    temperature = scrapeTemp()
    return str(temperature)

if __name__ == "__main__":
    with open('temperature.txt', 'w') as f:
        f.write(get_water_temperature())
        print(f"Temperature {get_water_temperature()} written to file.")
        input("Press any key to exit.")