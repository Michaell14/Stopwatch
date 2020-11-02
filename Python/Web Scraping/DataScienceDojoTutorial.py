from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as urlr

#csv
filename="products.csv"
f=open(filename, "w")
headers="brand, product_name, shipping\n"
f.write(headers)


#Source
source="https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+card"

client=urlr(source)

pagehtml=client.read()

client.close()

page_soup=bs(pagehtml, "html.parser")

#Grabs each project
containers=page_soup.findAll("div", {"class": "item-container"})
for container in range(len(containers)):
    print(containers[container].div.div.a.img["alt"])
    name=containers[container].findAll("a", {"class": "item-title"})
    price=containers[container].findAll("li", {"class": "price-current"})
    shipping_price=containers[container].findAll("li", {"class": "price-ship"})
    print("Brand name: "+name[0].text)
    print("Price: "+(price[0].text)[:-1])
    print("Shipping Price: "+shipping_price[0].text)
    print()
    f.write(name[0].text.replace(",", "|") +","+ price[0].text[:-1] +","+shipping_price[0].text+"\n")
f.close()
