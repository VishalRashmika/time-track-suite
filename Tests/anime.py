import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


myanimelist = "https://myanimelist.net/anime/49926/"
anilist = "https://anilist.co/anime/129874/s"

def get_anilist_data(anilist_url):
    response = requests.get(anilist_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = str(soup.find_all(class_="data-set"))
    soup2 = BeautifulSoup(text, 'html.parser')
    text2 = soup2.find_all(class_="value")
    episodes = str(str(text2[1]).split(">")[1]).split("<")[0]
    duration = str(str(text2[2]).split(">")[1]).split(" ")[0]
    runtime = int(duration) * int(episodes)

    return runtime

def get_myanimelist_data(my_animelist_url):
    response = requests.get(my_animelist_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    episodes = str(str(soup.find_all(class_="spaceit_pad")[4]).split(" ")[4]).strip("n")
    duration = str(soup.find_all(class_="spaceit_pad")[16]).split(" ")[4]
    runtime = int(duration) * int(episodes)

    return runtime

def calc_runtime(file_location):
    total_runtime = 0
    with open('export.json', 'r') as file:
        json_data = json.load(file)

        for items in json_data['Watched']:
            print(f"Name : {items['name']} | AniList : {items['al']} | MyAnimeList : {items['mal']}")
    file.close()
    return total_runtime

calc_runtime("d")