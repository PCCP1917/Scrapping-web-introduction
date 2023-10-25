import requests
from bs4 import BeautifulSoup
import re

#Get URL
url="https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)
html=response.content
#Analize HTML using BeutifulSoup
soup = BeautifulSoup(html,"html.parser")
#Get Page title
page_title = soup.title.string
print(f"El título es: {page_title}")
print("_"*100)
#Get links in page
links = []
for link in soup.find_all("a", href=True):
    if "http" in link["href"]:
        links.append(link["href"])
print(links)
print("_"*100)
#Get all headers
headers = []
for header in soup.find_all(re.compile("^h[1-6]$")):
    headers.append(header.text.strip())
print(headers)
print("_"*100)
#Get Main picture on this page
img= soup.find("img",{"src":"//upload.wikimedia.org/wikipedia/commons/thumb/9/94/Guido_van_Rossum_OSCON_2006_cropped.png/150px-Guido_van_Rossum_OSCON_2006_cropped.png"})
img_url="https:" + img["src"]
print(f"La imágen es {img_url}")
print("_"*100)