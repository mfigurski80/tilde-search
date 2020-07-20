from pdb import set_trace as tr

from data import *
from parse_html import *
from tokenize_corpus import tokenize


def crawl_sites(batch=20):
    dictionary = read_document_frequency()
    to_crawl = read_sites()
    tags, sites = read_results()

    while len(to_crawl) > 0:
        s = to_crawl.pop(0)
        print(f'Crawl #{len(sites)}->#{len(to_crawl)}: {s}')
        tags_data, metadata = parse_url(s, dictionary)
        sites[url] = metadata
        for t in tags_data:
            if t[0] not in tags:
                tags[t[0]] = []
            tags.append(t)

        if len(sites) % batch == 0:
            write_results(tags, sites)
    pass
    write_results(tags, sites)


def read_results():
    return read_tags(), read_sites()


def write_results(tags, sites):
    return write_tags(tags), write_sites(sites)


if __name__ == '__main__':
    crawl_sites()
