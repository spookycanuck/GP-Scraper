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

time_length = len(time)
for x in range(time_length):
    if (time[x].find('.')==1):
        time[x] = time[x].replace(time[x], "Race Completed")
    elif (time[x].find('Canceled')==0):
        time[x] = time[x].replace(time[x], "Race has been CANCELED")

watch_length = len(watch)
for x in range(watch_length):
    if not bool(watch[x]):
        watch[x] = watch[x].replace(watch[x], "N/A")

dates_length = len(date)
for x in range(dates_length):
    # print(date[x])
    month = date[x].split(' ')
    if (len(month) <= 4):
        date[x] = month[0] + ' ' + month[-1]
    else:
        date[x] = month[-2] + ' ' + month[-1]

title_length = len(title)
for x in range(title_length):
    title[x] = title[x].replace("GP", "Grand Prix")

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
#   write results to CSV w/ headers.