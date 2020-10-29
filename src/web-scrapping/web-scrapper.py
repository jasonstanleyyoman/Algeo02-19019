#!/usr/bin/env python
import requests
import json
from bs4 import BeautifulSoup

def start():
    print("Hello world")
    success = 0
    all_links = []
    all_title = []
    all_data = []
    URL = "https://myanimelist.net/topanime.php?limit=0"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    i = 0
    for table_row in soup.find_all("tr"):
        link = table_row.find("a")
        try :
            data = ""
            anime_link = link.get("href")
            print("Link :")
            print(anime_link)

            anime_page = requests.get(anime_link)
            anime_soup = BeautifulSoup(anime_page.content,'html.parser')

            # Get Title
            print("Title :")
            anime_title = anime_soup.find(class_="title-name h1_bold_none").text
            data += (anime_title + " ") * 10

            data += " "



            # Get Synopsis
            print("Synopsis : ")
            synoposis = anime_soup.find(itemprop="description").text
            data += synoposis

            # Get Alternative Title
            alternative = anime_soup.find_all("div", class_="spaceit_pad")
            print("Alternative : ")
            for alt in alternative :
                if alt.find("span") != None:
                    data += alt.text

            # Get Character, Voice Actor, Staff
            print("Character, Voice Actor, Staff : ")
            containers = anime_soup.find_all("div", class_="detail-characters-list clearfix")
            for container in containers :
                all_character = container.find_all("a")
                for character in all_character:
                    data += character.text.lstrip().rstrip()

            # Get Opening Theme
            print("Opening Theme : ")
            all_opening = anime_soup.find("div", class_="theme-songs js-theme-songs opnening").find_all("span")
            for opening in all_opening:
                data += opening.text

            # Get Ending Theme
            print("Ending Theme : ")
            all_ending = anime_soup.find("div", class_="theme-songs js-theme-songs ending").find_all("span")
            for ending in all_ending:
                data += ending.text

            # Get Genre and Producers
            print("Genre : ")
            all_genre_and_producer = [link.text for link in anime_soup.find_all("a") if link.get("href") and (link.get("href").find("genre") != -1 or link.get("href").find("producer") != -1)]
            for genre_and_producer in all_genre_and_producer :
                data += genre_and_producer + " "

            all_title.append(anime_title)
            all_links.append(anime_link)
            all_data.append(data)

            print(data)
            success += 1

        except:
            print("Error")
            print(link)
        i += 1
        # Sementara ambil 9 data dulu
        if i == 10:
            print("Successfullly get information of this anime")

            break
    for title in all_title :
        print(title)
    with open('titles.json', 'w') as file:
        json.dump(all_title, file)
    with open('links.json', 'w') as file:
        json.dump(all_links, file)
    with open('data.json', 'w') as file:
        json.dump(all_data, file)

if __name__ == "__main__" :
    start()
