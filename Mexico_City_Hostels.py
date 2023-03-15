import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep

URL = [
    "https://www.hostelworld.com/st/hostels/p/307620/casa-kanabri-hostal-boutique/",
    "https://www.hostelworld.com/st/hostels/p/310035/wanderlust-district/",
]


# for url in range(0, 2):


name_list = []


def hostel_names_list():
    hostel_name = soup.find("h1")
    hostel_name = hostel_name.text.strip()
    name_list.append(hostel_name)
    return name_list


# print(f"\nHostel Name: {name_list}")
compiled_names = hostel_names_list()

hostel_scores = []
composite_hostel_scores = []


def hostel_scores_list():
    breakdown_scores = soup.find_all("div", class_="rating-score")

    for breakdown_score in breakdown_scores:
        breakdown_score = breakdown_score.text.strip()
        hostel_scores.append(breakdown_score)

    # print(f"\nHostel scores: {hostel_scores}")

    composite_hostel_scores.append(hostel_scores)
    return composite_hostel_scores


print(f"\nComposite scores: {composite_hostel_scores}")
composite_scores = hostel_scores_list()


def hostel_dictionary(keys: list, values: list):
    lists_to_join = zip(keys, values)
    # print(f"\nLists to join: {lists_to_join}\n")
    specific_ratings = list(lists_to_join)
    # print(f"\nSpecific ratings: {specific_ratings}\n")
    ratings_dict = dict(specific_ratings)
    return ratings_dict


complete_dictionary = hostel_dictionary(compiled_names, composite_scores)
print(f"\nRatings Dictionary: {complete_dictionary}\n")


def compare_hostels():
    for url in range(0, 2):
        page = requests.get(URL[url], timeout=10)
        soup = BeautifulSoup(page.content, "html.parser")
        soup.prettify()
        hostel_names_list()
        hostel_scores_list()
        hostel_dictionary(compiled_names, composite_scores)


compare_hostels()


# def hostel_dictionary(keys: list, values: list):
#     lists_to_join = zip(name_list, composite_hostel_scores)
#     # print(f"\nLists to join: {lists_to_join}\n")
#     specific_ratings = list(lists_to_join)
#     # print(f"\nSpecific ratings: {specific_ratings}\n")
#     ratings_dict = dict(specific_ratings)
#     return ratings_dict


# complete_dictionary = hostel_dictionary
# print(f"\nRatings Dictionary: {complete_dictionary}\n")


# def compare_hostels():
#     for url in range(0,2):
# name function
# list of specific ratings
# create dictionary
# data frame
# csv
