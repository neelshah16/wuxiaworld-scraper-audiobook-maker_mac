from bs4 import BeautifulSoup
import requests
import os

BASE_URL = "https://www.wuxiaworld.co/The-Strongest-Gene/"
AGENT_HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def content_preprocessing(raw:str):
    raw = raw.replace('<br/>', ' ')
    raw = raw.replace('\t', ' ')
    raw = raw.replace('\n', ' ')
    raw = raw.replace('</div>', ' ')
    raw = raw.replace('<script>chaptererror();</script>', ' ')
    raw = raw.replace("""<div id="content">""", ' ')
    return raw

with open('list_of_pages.txt') as f:
    lines = f.read().splitlines()

for i_, i in enumerate(lines):
    [url, title] = i.split('||')
    print("Scraping %s" % title)
    page_data = requests.get(BASE_URL+url, headers=AGENT_HEADERS).text
    soup = BeautifulSoup(page_data, "html.parser")
    content = content_preprocessing(str(soup.select("#content")[0]))
    print(content)
    os.system("""say -r 350 -v "Veena" "%s" -o audiobook/base.aiff; lame -m m "audiobook/base.aiff" "audiobook/%s.mp3" """ % (
        content.replace('"', "'"),
        title.replace(":", " -")
    ))


