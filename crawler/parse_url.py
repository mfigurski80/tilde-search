import urllib.request
import urllib.parse
import re
import math
from bs4 import BeautifulSoup as bs4
from pdb import set_trace as tr

from tokenize_corpus import tokenize


def get_site(url):
    url = urllib.parse.quote(url)
    try:
        return urllib.request.urlopen(f'http://tilde.club/{url}').read()
    except urllib.error.HTTPError as e:
        raise FileNotFoundError(f'{url} not found')


def parse_text(html):
    soup = bs4(html, features='html.parser')
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    text = soup.get_text()
    text = re.sub('[^a-zA-Z\']+', ' ', text).strip()
    return text


def parse_tags_tfidf(html, dict):
    tokens = tokenize(parse_text(html))
    tf = {k: tokens.count(k) / len(tokens) for k in tokens}
    idf = {k: math.log(dict['count'] / dict['data'][k]) if k in dict['data']
           else math.log(dict['count'] / 1) for k in tf}
    tfidf = {k: round(tf[k] * idf[k], 5) for k in tf}
    return tfidf


def parse_user(url):
    match = re.search('~\w+', url)
    if match is None:
        return None
        # raise Exception(f'No user could be found in url: {url}')
    return match.group().replace('~', '')


def is_tilde(url):
    return 'tilde.club' in url


def parse_links(soup, url):
    user = parse_user(url)
    links = [l['href'].split('?')[0].split('#')[0] for l in soup.find_all('a', href=True)]
    links = [l for l in links if l != url]
    # TODO: add domain to relative links
    links = [l for l in links if not l.startswith('/')]
    # links = [url + l for l in links if l.startswith('/') else l]

    links_user = ['~' + l.split('~')[1] for l in links if is_tilde(l) and parse_user(l) == user]
    links_domain = ['~' + l.split('~')[1] for l in links if is_tilde(l)
                    and parse_user(l) != user and parse_user(l) != None]
    links_exterior = [l for l in links if not is_tilde(l)]
    return links_user, links_domain, links_exterior


def Metadata(
    size=0,
    title='',
    hash=0,
    avg_tfidf=0,
    linked_user=0,
    linked_domain=0,
    links_user=0,
    links_domain=0,
    links_exterior=0
):
    return {
        'size': size,
        'title': title,
        'hash': hash,
        'avg_tfidf': avg_tfidf,
        'linked_user': linked_user,
        'linked_domain': linked_domain,
        'links_user': links_user,
        'links_domain': links_domain,
        'links_exterior': links_exterior
    }


def parse_url(url, dictionary):
    html = get_site(url)
    soup = bs4(html, features='html.parser')

    tfidf = parse_tags_tfidf(html, dictionary)
    limit_tfidf = round(sum(tfidf.values())/max(len(tfidf), 1) * 1.0, 5)
    tags = {k: tfidf[k] for k in tfidf if tfidf[k] >= limit_tfidf}

    links_user, links_domain, links_exterior = parse_links(soup, url)
    title = None
    if soup.title is not None:
        title = soup.title.text
    metadata = Metadata(
        size=len(html),
        title=title,
        hash=hash(html) % 1048576,
        avg_tfidf=limit_tfidf,
        linked_user=[],
        linked_domain=[],
        links_user=links_user,
        links_domain=links_domain,
        links_exterior=links_exterior
    )
    return tags, metadata
