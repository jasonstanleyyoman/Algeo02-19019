# Chika Engine 
> A search engine for searching the latest informations for anime, manga, and so on.\
> [Spesifikasi Tubes](https://drive.google.com/file/d/1YThhhPhrX3xce4vwtH8fGhKR4euv_HSX/view) | [Laporan](https://docs.google.com/document/d/1wVcsBjCHXk4DWX5mus3BnXL9-69UUYrisBg9_Wo6zrI/edit?ts=5f9bc110)

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
Add more general information about project. What the purpose of the project is? Motivation?

## Screenshots
![Example screenshot](./img/screenshot.png)

## Technologies
* Tech 1 - version 1.0
* Tech 2 - version 2.0
* Tech 3 - version 3.0

## Setup
Clone repository 
```sh
git clone https://github.com/jasonstanleyyoman/Algeo02-19019.git
```
#### Install semua dependencies
##### Backend
Pengguna diharapkan sudah menginstall python3 dan pip3 di mesinnya. Jika belum silahkan kunjungi laman berikut untuk panduan instalasinya
<br/>
[Instalasi python3 dan pip3](https://www.python.org/downloads/)
<br/>
Setelah itu install dependencies pythonnya dengan cara yang disesuaikan dengan sistem operasi yang Anda gunakan
- [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [nltk](https://www.nltk.org/install.html)
- [numpy](https://numpy.org/install/)
- [pdftotext](https://pypi.org/project/pdftotext/)
- [requests](https://requests.readthedocs.io/en/master/user/install/#install)

<br/>
Jalankan backend dengan menggunakan command ini
<br/>
```sh
cd src/server
python3 app.py
```
<br/>
##### Frontend
Pengguna diharapkan sudah menginstall nodejs dan package manager (npm atau yarn) di mesinnya. Jika belum silahkan kunjungi laman berikut untuk panduan instalasinya

[Node JS](https://nodejs.org/en/download/)
[yarn](https://classic.yarnpkg.com/en/docs/install/#debian-stable)

Jalankan frontend dengan menggunakan command ini
```sh
cd src/chika-engine
npm install # yarn install jika menggunakan yarn
npm start
```

## Code Examples
#### Web Scrapping
Jika ingin menggunakan web scrapping untuk mengambil data, execute command ini
```sh
python3 src/server/web-scrapping/web-scrapper.py ${JumlahDokumen} # Ganti ${JumlahDokumen} dengan jumlah dokumen yang ingin diambil
```
Contoh :
```sh
python3 src/server/web-scrapping/web-scrapper.py 30
```

Setelah itu jalankan command ini untuk memproses data yang diambil
```sh
python3 src/server/preprocess.py
python3 src/server/total_words.py
python3 src/server/get_15_word.py
```

## Features
List of features ready and TODOs for future development
* Awesome feature 1
* Awesome feature 2
* Awesome feature 3

To-do list:
- [ ] Web Scraping (?)
- [ ] Backend (?)
- [ ] Frontend (?)


## Status
Project is: _in progress_

## Inspiration
Add here credits. Project inspired by..., based on...

## Contact
Created by [@jasonstanleyyoman](), [@cyn-rus](), and [@salyamevia]().
