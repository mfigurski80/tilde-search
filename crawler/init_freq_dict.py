import urllib.request
import re
from bs4 import BeautifulSoup as bs4
from pdb import set_trace as tr

from data import *
from tokenize_corpus import tokenize


def get_site(url):
    return urllib.request.urlopen(url).read()


def parse_text(html):
    soup = bs4(html)
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    text = soup.get_text()
    text = re.sub('[^a-zA-Z\']+', ' ', text).strip()
    return text


def make_document_frequency_dict(batches=20):
    n, last, frequency = read_json(
        './document_frequency.json',
        {'count': 0, 'last': None, 'data': {}}
    ).values()

    sites = read_sites()
    if last is not None and n > 0:
        if sites[n-1] == last:
            sites = sites[n:]
        else:
            sites = sites[sites.index(last):]

    for i, s in enumerate(sites):
        if len(s) <= 0:
            continue
        print(f'{i}+{n}: {s}')
        html = get_site(s)
        text = parse_text(html)
        tokens = list(set(tokenize(text)))
        for word in tokens:
            if word not in frequency:
                frequency[word] = 0
            frequency[word] += 1
        n += 1
        last = s
        if (i + 1) % batches == 0:  # save in batches
            write_json('./document_frequency.json', {'count': n, 'last': last, 'data': frequency})

    write_json('./document_frequency.json', {'count': n, 'last': last, 'data': frequency})


if __name__ == '__main__':
    make_document_frequency_dict()
