from data import *
from parse_url import *
from tokenize_corpus import tokenize


def make_document_frequency_dict(batch=20):
    n, last, frequency = read_document_frequency().values()

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
        if (i + 1) % batch == 0:  # save in batches
            write_document_frequency({'count': n, 'last': last, 'data': frequency})

    write_document_frequency({'count': n, 'last': last, 'data': frequency})


if __name__ == '__main__':
    make_document_frequency_dict()
