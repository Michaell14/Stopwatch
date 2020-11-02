from bs4 import BeautifulSoup as bs
import requests

website=requests.get("https://www.josh.org/inspiration-see-yourself-as-loved-by-god/").text
soup=bs(website, "lxml")


# for article in soup.find_all("p"):
# 	#summer=article.find("span", class_="s1").text

# 	try:
# 		summer=article.find("span", class_="s1").text
# 		print(summer)

# 		# summer_list=summer.split(".")
# 		# for i in summer_list:
# 		# 	print(i)

# 	except Exception:
# 		pass

for article in soup.find_all("a"):
	try:
		image=article.find("img", class_="size-large wp-image-55011 borderless square")["src"]
		print(image)
	except Exception:
		pass