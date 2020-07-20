import urllib.request
import re
from bs4 import BeautifulSoup as bs4

from tokenize_corpus import tokenize


def get_site(url):
    return urllib.request.urlopen(url).read()


def parse_text(html):
    soup = bs4(html, features='html.parser')
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    text = soup.get_text()
    text = re.sub('[^a-zA-Z\']+', ' ', text).strip()
    return text


def parse_tags_data(html, dict):
    text = parse_text()
    pass


def parse_metadata(html):
    pass


def parse_url(url, dictionary):
    html = get_site(url)
    tags_data = parse_tags_data(html, dictionary)
    metadata = parse_metadata(html)
    return tags_data, metadata
