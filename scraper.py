import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup


def get_rss_headlines(url, limit=20):
    response = requests.get(url)
    root = ET.fromstring(response.content)

    headlines = []

    for item in root.findall(".//item")[:limit]:
        title = item.findtext("title", default="")
        link = item.findtext("link", default="")
        pub_date = item.findtext("pubDate", default="")

        if not link:
            link = item.findtext("guid", default="")

        headlines.append({
            "title": title,
            "link": link,
            "date": pub_date
        })

    return headlines