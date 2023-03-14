import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

URL = "https://www.hostelworld.com/st/hostels/p/307620/casa-kanabri-hostal-boutique/"
page = requests.get(URL, timeout=10)

soup = BeautifulSoup(page.content, "html.parser")
soup.prettify()

hostel_name = soup.find("h1")
# print(hostel_name.text.strip())

hostel_rating = soup.find("div", class_="score orange big")
hostel_rating = hostel_rating.text.strip()

hostel_reviews = soup.find("div", class_="reviews")
hostel_reviews = hostel_reviews.text.strip()


hostel_reviews = str(hostel_reviews)
# print(f"string version is: {hostel_reviews}")

remove_words = ["Total", "Reviews"]

for word in remove_words:
    hostel_reviews = hostel_reviews.replace(word, "")
print(f"\nRemoved words from hostel reviews: {hostel_reviews}")

# hostel_reviews = hostel_reviews.replace("")

ratings_breakdown = soup.find_all("div", class_="rating-label")

headings = []
for rating_breakdown in ratings_breakdown:
    rating_breakdown = rating_breakdown.text.strip()
    headings.append(rating_breakdown)
print(headings)

breakdown_scores = soup.find_all("div", class_="rating-score")

scores = []

for breakdown_score in breakdown_scores:
    breakdown_score = breakdown_score.text.strip()
    scores.append(breakdown_score)
print(scores)

lists_to_join = zip(headings, scores)
specific_ratings = list(lists_to_join)
ratings_dict = dict(specific_ratings)
print(ratings_dict)
