from pdb import set_trace as tr

from data import *
from parse_url import *
from tokenize_corpus import tokenize


def crawl_sites(batch=20):
    dictionary = read_document_frequency()
    to_crawl = read_sites()
    tags, sites_meta = read_results()

    while len(to_crawl) > 0:
        s = to_crawl.pop(0)
        if len(s) <= 0:
            continue
        print(f'Crawl #{len(to_crawl)}->#{len(sites_meta)} : {s}')

        tags_data, metadata = parse_url(s, dictionary)
        # handle tag data
        for t in tags_data:
            if t not in tags:
                tags[t] = {}
            tags[t][s] = tags_data[t]
        # handle metadata
        for l in metadata['links_user']:
            if l not in sites_meta:
                sites_meta[l] = Metadata()
            sites_meta[l]['linked_user'] += 1
        for l in metadata['links_domain']:
            if l not in sites_meta:
                sites_meta[l] = Metadata()
            sites_meta[l]['linked_domain'] += 1
        if s not in sites_meta:
            sites_meta[s] = Metadata()
        metadata['links_user'] = len(metadata['links_user'])
        metadata['links_domain'] = len(metadata['links_domain'])
        metadata['links_exterior'] = len(metadata['links_exterior'])
        metadata['linked_user'] = sites_meta[s]['linked_user']
        metadata['linked_domain'] = sites_meta[s]['linked_domain']
        sites_meta[s] = metadata

        if len(to_crawl) % batch == 0:
            write_results(tags, sites_meta)
    pass
    write_results(tags, sites_meta)


def read_results():
    return read_tags(), read_metadata()


def write_results(tags, metadata):
    return write_tags(tags), write_metadata(metadata)


if __name__ == '__main__':
    crawl_sites()
