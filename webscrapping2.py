import csv
from unicodedata import name 
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import pandas as pd 

START_URL = (
    "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
)
wiki = requests.get(START_URL)
soup = BeautifulSoup(wiki.text, "html.parser")

temp_list = []
for tr in soup.find("table").find_all("tr"):
    td = tr.find_all("td")
    row = [i.text.strip() for i in td]
    temp_list.append(row)

Star = []
Distance = []
Mass = []
Radius = []

for i in range(1, len(temp_list)):
    Star.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])

df = pd.DataFrame(
    list(zip(Star, Distance, Mass, Radius)),
    columns=["Star_name", "Distance", "Mass", "Radius"],
)


df.to_csv("brown_dwraf_data.csv")