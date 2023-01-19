from bs4 import BeautifulSoup
import requests
import os

output_dir = "transcripts/"

url = "https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media"  
headers = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(url, headers=headers)
soup = BeautifulSoup(webpage.content, "html.parser")
rows = soup.find_all("table", class_ = "table-dotted-rows")

transcript_urls = []

season = 1

def write(url, season):
    webpage = requests.get(url, headers=headers)
    soup = BeautifulSoup(webpage.content, "html.parser")

    content = soup.find("textarea")

    name = url.split('/')[-1].split('?')[0]
    data = content.text

    os.makedirs("season_" + str(season), exist_ok=True)

    f = open("season_" + str(season) + "/" + name + ".txt", "w")
    f.write(data)
    f.close()

    print("Wrote {}".format(name))

for row in rows:
    links = row.find_all("a")

    for link in links:
        if link.text == "Transcript":
            write("https://mlp.fandom.com" + link.get('href') + "?action=edit", season)

    season += 1


