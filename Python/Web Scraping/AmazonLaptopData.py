from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as urlo
import requests

source=requests.get("https://www2.montgomeryschoolsmd.org/schools/woottonhs/").text
page_soup=bs(source, "lxml")

#client=urlo(source)
#pagehtml=client.read()
#client.close()

#page_soup=bs(pagehtml, "html.parser")

containers=page_soup.findAll("a",class_="list-group-item list-group-item-action")
for container in containers:
    name=container.h3.text
                             
    print(name)
