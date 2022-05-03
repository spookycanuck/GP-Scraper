import requests
import csv
import xlsxwriter
from bs4 import BeautifulSoup


##### Scraping from Web #####

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
        watch[x] = watch[x].replace(watch[x], "No info available")
    watch[x] = watch[x].replace('Highlights', "N/A")

title_length = len(title)
for x in range(title_length):
    title[x] = title[x].replace("GP", "Grand Prix")


##### Writing to file #####
## For some reason, one of the code blocks has to be commented out or else it breaks

headers = ['Date', 'Race', 'Location', 'Lights Out', 'Watch']
data = [date,title,location,time,watch]

# writing to an xlsx file
# with xlsxwriter.Workbook('files/schedule.xlsx') as workbook:
#     worksheet = workbook.add_worksheet()
#     for row_num, data in enumerate(data):
#         # print (row_num, headers[row_num],i)
#         worksheet.write_row(row_num, 0, [headers[row_num]])
#         worksheet.write_row(row_num, 1, data)

# writing to csv file 
with open('files/schedule.csv', 'w') as csvfile: 
    wr = csv.writer(csvfile) 
    for row_num, data in enumerate(data):
        wr.writerow([headers[row_num]])
        wr.writerow(data)

