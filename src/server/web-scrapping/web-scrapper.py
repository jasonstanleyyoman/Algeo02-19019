#!/usr/bin/env python
import requests
import json
import sys
from bs4 import BeautifulSoup
TOTAL_ANIME = 10
def start():
    all_links = []
    all_title = []
    all_data = []
    all_synopsis = []
    URL = "https://myanimelist.net/topanime.php?limit=0"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    i = 0
    for table_row in soup.find_all("tr"):
        link = table_row.find("a")
        try :
            data = ""
            anime_link = link.get("href")

            anime_page = requests.get(anime_link)
            anime_soup = BeautifulSoup(anime_page.content,'html.parser')

            # Get Title
            anime_title = anime_soup.find(class_="title-name h1_bold_none").text
            data += (anime_title + " ") * 20

            data += " "



            # Get Synopsis
            synoposis = anime_soup.find(itemprop="description").text
            data += synoposis

            # Get Alternative Title
            alternative = anime_soup.find_all("div", class_="spaceit_pad")
            for alt in alternative :
                if alt.find("span") != None:
                    data += alt.text

            # Get Character, Voice Actor, Staff
            containers = anime_soup.find_all("div", class_="detail-characters-list clearfix")
            for container in containers :
                all_character = container.find_all("a")
                for character in all_character:
                    data += (character.text.lstrip().rstrip() + " ") * 5

            # Get Opening Theme
            all_opening = anime_soup.find("div", class_="theme-songs js-theme-songs opnening").find_all("span")
            for opening in all_opening:
                data += (opening.text + " ") * 8

            # Get Ending Theme
            all_ending = anime_soup.find("div", class_="theme-songs js-theme-songs ending").find_all("span")
            for ending in all_ending:
                data += (ending.text + " ") * 8

            # Get Genre and Producers
            all_genre_and_producer = [link.text for link in anime_soup.find_all("a") if link.get("href") and (link.get("href").find("genre") != -1 or link.get("href").find("producer") != -1)]
            for genre_and_producer in all_genre_and_producer :
                data += (genre_and_producer + " ") * 5

            all_title.append(anime_title)
            all_links.append(anime_link)
            all_data.append(data)
            all_synopsis.append(synoposis)
            print(anime_title + " Finished fetching")

        except Exception as err:
            print("Error")
        i += 1
        # Sementara ambil 9 data dulu
        if i == TOTAL_ANIME + 1:
            break
    print("--------------------------------------")
    print("--------------------------------------")
    print("Finish Fetching this Anime : ")
    for title in all_title :
        print("-- " + title)
    with open('titles.json', 'w') as file:
        json.dump(all_title, file)
    with open('links.json', 'w') as file:
        json.dump(all_links, file)
    with open('data.json', 'w') as file:
        json.dump(all_data, file)
    with open('synoposis.json', 'w') as file:
        json.dump(all_synopsis, file)
if __name__ == "__main__" :
    if len(sys.argv) != 2 :
        print("Usage : python3 web-scrapper.py ${AnimeTotal}")
    else :
        try :
            total_anime = int(sys.argv[1])
            TOTAL_ANIME = total_anime
            start()
        except Exception as err:
            print("AnimeTotal must be integer")
