import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.espn.com/f1/schedule")
soup = BeautifulSoup(page.content, "html.parser")
home = soup.find(class_="Table__TBODY")
posts = home.find_all(class_="Table__TR Table__TR--sm Table__even")

date = []
title = []
location = []
time = []
watch = []
x = []

for post in posts:
    date.append(post.find(class_="date__col Table__TD").text.strip())
    title.append(post.find("a", class_="AnchorLink").text.strip())
    x.append(post.find(class_="race__col Table__TD"))
    for each in x:
        loc = (each.find("div").text.strip())
    location.append(loc)
    time.append(post.find(class_="winnerLightsOut__col Table__TD").text.strip())
    watch.append(post.find(class_="tv__col Table__TD").text.strip())

print("Dates:")
print(date)
print("------------------")
print("Title:")
print(title)
print("------------------")
print("Locations:")
print(location)
print("------------------")
print("Times:")
print(time)
print("------------------")
print("Where to watch:")
print(watch)

# TODO:
#   check times for a . character and omit the value, replace with n/a.
#   check watch for an empty set, replace with n/a.
#   replace dates w/ first 3 & last 2 characters of the string?
#   write results to CSV w/ headers.