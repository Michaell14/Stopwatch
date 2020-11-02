from bs4 import BeautifulSoup as bs
import requests
import csv

source=requests.get("https://ceoworld.biz/2020/05/10/ranked-worlds-best-countries-for-education-system-2020/#:~:text=The%20world%E2%80%99s%20best%20countries%20for%20the%20education%20system%2C,%20%2067.21%20%2082%20more%20rows%20").text
pageSoup=bs(source, "lxml")
csvFile=open("CountryEducationRankings.csv", "w")
write=csv.writer(csvFile)

ranks=[]
countries=[]
qualityIndex=[]
opportunityIndex=[]
headings=[]

for container in pageSoup.findAll("tr"):
    for heading in container.findAll("th"):
        headings.append(heading.text)
    for rank in container.findAll("td" , {"class": "column-1"}):
        ranks.append(rank.text)
    for country in container.findAll("td" , {"class": "column-2"}):
        countries.append(country.text)

    for quality in container.findAll("td" , {"class": "column-3"}):
        qualityIndex.append(quality.text)
    for opportunity in container.findAll("td" , {"class": "column-4"}):
        opportunityIndex.append(opportunity.text)

write.writerow(",".join(headings))
for i in range(len(countries)):
    write.writerow([ranks[i]+","+countries[i]+","+qualityIndex[i]+","+opportunityIndex[i]])

