import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# with open('export.json', 'r') as file:
#     json_data = json.load(file)

# for key, value in json_data.items():
#     # print(key + ':' + str(value))
#     for i in range(0,len(value)):
#         print(value[i]['name'])

myanimelist = "https://myanimelist.net/anime/49926/"
anilist = "https://anilist.co/anime/129874/s"

def get_anilist_data(anilist_url):
    response = requests.get(anilist_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = str(soup.find_all(class_="data-set"))
    # text2 = str(text.find_all(class_="type"))

    return text

print(get_anilist_data(anilist))