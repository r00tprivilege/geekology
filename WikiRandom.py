#install packages: htmlparser & beatifulsoup4
from bs4 import BeautifulSoup
import requests

# Trying to open a random wikipedia article
# Special:Random opens random articles
rqst = requests.get("https://en.wikipedia.org/wiki/Special:Random")
rqst.raise_for_status()
# pip install htmlparser
wiki = BeautifulSoup(rqst.text, "html.parser")
rq = open("random_wiki.txt", "w+", encoding='utf-8')
# Adding the heading to the text file
heading = wiki.find("h1").text
rq.write(heading + "\n")
for i in wiki.select("p"):
    # Optional Printing of text
    # print(i.getText())
    rq.write(i.getText())

rq.close()
print("File Saved as random_wiki.txt")
