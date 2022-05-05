import requests
import csv
import xlsxwriter
from bs4 import BeautifulSoup


##### Scraping from Web #####

page = requests.get("https://www.espn.com/f1/schedule")
soup = BeautifulSoup(page.content, "html.parser")
home = soup.find(class_="Table__TBODY")
posts = home.find_all(class_="Table__TR Table__TR--sm Table__even")

output_list = []

for post in posts:
    date = post.find(class_="date__col Table__TD").text.strip()
    title = post.find("a", class_="AnchorLink").text.strip()
    location = post.find(class_="race__col Table__TD").find("div").text.strip()
    time = post.find(class_="winnerLightsOut__col Table__TD").text.strip()
    watch = post.find(class_="tv__col Table__TD").text.strip()

    if (time.find('.')==1):
        time = time.replace(time, "Race Completed")
        watch = watch.replace('Highlights', "N/A")
    elif (time.find('Canceled')==0):
        time = time.replace(time, "Race has been CANCELED")
    
    if not bool(watch):
        watch = watch.replace(watch, "No info available")

    race_dict = {
        "date": date,
        "race": title,
        "location": location,
        "time": time,
        "watch": watch
    }

    output_list.append(race_dict)


##### Writing to CSV #####

headers = ['date', 'race', 'location', 'time', 'watch']

# writing to file 
with open('files/schedule4.csv', 'w') as csvfile: 
    wr = csv.DictWriter(csvfile, fieldnames=headers) 
    wr.writeheader()
    wr.writerows(output_list)
