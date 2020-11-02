from bs4 import BeautifulSoup as bs
import requests
import csv

source=requests.get("https://coreyms.com/").text
soup=bs(source, "lxml")
csv_file=open("cms_scrape.csv", "w")
csv_writer=csv.writer(csv_file)
csv_writer.writerow(["headline", "summary", "video link"])
for article in soup.find_all("article"):

	summary=article.find("div", class_="entry-content").p.text
	print(summary)
	headline=article.h2.a.text
	#print(article.prettify())
	# print(article.h2.a.text)
	try:
		vid_src=article.find("iframe", class_="youtube-player")["src"]
		# # print(vid_src)

		vid_id=vid_src.split("/")[4]
		vid_id=vid_id.split("?")[0]
		yt_link=f"https://youtube.com/watch?v={vid_id}"
	except Exception:
		yt_link=None
	# print(vid_id)

	print(yt_link)
	csv_writer.writerow([headline, summary, yt_link])
csv_file.close()