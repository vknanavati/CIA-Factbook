import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

URL = "https://www.cia.gov/the-world-factbook/countries/switzerland/travel-facts"
page = requests.get(URL, timeout=10)

soup = BeautifulSoup(page.content, "html.parser")
soup.prettify()

headings = []
data = []
for topic in soup.find_all("h3"):
    headings.append(topic.text)

    info = topic.find_next_sibling("p")
    data.append(info.text)

lists_to_join = zip(headings, data)
joint_list = list(lists_to_join)


country_dict = dict(joint_list)

with open("country_dict.json", encoding="UTF-8") as country_dict_list:
    country_dict_list = country_dict_list.read()
print(f"data:{country_dict_list}")

country_dict_list = json.loads(country_dict_list)

keys = {
    "US State Dept Travel Advisory",
    "Climate",
    "Currency",
    "Major Languages",
    "Road Driving Side",
    "Tourist Destinations",
    "Cultural Practices",
    "Tipping Guidlines",
    "Traditional Cuisine",
}
new_dict = {key: value for key, value in country_dict.items() if key in keys}
print(new_dict)
