import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

with open('export.json', 'r') as file:
    json_data = json.load(file)

for key, value in json_data.items():
    # print(key + ':' + str(value))
    for i in range(0,len(value)):
        print(value[i]['name'])



# url = "helll"

# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# text = str(soup.find_all(class_="text-link text-footer"))