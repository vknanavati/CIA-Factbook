import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep

URL = [
    "https://www.hostelworld.com/st/hostels/p/307620/casa-kanabri-hostal-boutique/",
    "https://www.hostelworld.com/st/hostels/p/310035/wanderlust-district/",
]


name_list = []


def name_of_hostel():
    for url in range(0, 2):
        page = requests.get(URL[url], timeout=10)
        soup = BeautifulSoup(page.content, "html.parser")
        soup.prettify()
        hostel_name = soup.find("h1")
        hostel_name = hostel_name.text.strip()
        name_list.append(hostel_name)

    print(f"\nHostel Name: {name_list}")


name_of_hostel()


hostel_rating = soup.find("div", class_="score orange big")
hostel_rating = hostel_rating.text.strip()
print(f"\nHostel Rating: {hostel_rating}")

hostel_reviews = soup.find("div", class_="reviews")
hostel_reviews = hostel_reviews.text.strip()

hostel_reviews = str(hostel_reviews)
# print(f"string version is: {hostel_reviews}")

remove_words = ["Total", "Reviews"]

for word in remove_words:
    hostel_reviews = hostel_reviews.replace(word, "")
print(f"\nNumber of Reviews: {hostel_reviews}")

# hostel_reviews = hostel_reviews.replace("")

ratings_breakdown = soup.find_all("div", class_="rating-label")

headings = []
for rating_breakdown in ratings_breakdown:
    rating_breakdown = rating_breakdown.text.strip()
    headings.append(rating_breakdown)
print(f"\nList of headings: {headings}")

breakdown_scores = soup.find_all("div", class_="rating-score")

scores = []

for breakdown_score in breakdown_scores:
    breakdown_score = breakdown_score.text.strip()
    scores.append(breakdown_score)
print(f"\nList of scores: {scores}")

lists_to_join = zip(headings, scores)
specific_ratings = list(lists_to_join)
ratings_dict = dict(specific_ratings)
print(f"\nRatings Dictionary: {ratings_dict}\n")

sleep(randint(2, 10))
