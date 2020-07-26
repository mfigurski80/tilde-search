import json


# GENERAL Interfaces

def read_json(file, default=None):
    try:
        with open(file) as infile:
            return json.load(infile)
    except FileNotFoundError as e:
        return default


def write_json(file, obj):
    with open(file, 'w') as outfile:
        json.dump(obj, outfile)


# FILE SPECIFIC Interfaces

def read_sites():
    with open('../discovery/sites.txt') as f:
        data = f.read().split('\n')
        f.close()
        return data


def write_sites(data):
    with open('../discovery/sites.txt', 'w') as f:
        f.write(data)
        f.close()


def read_document_frequency():
    default = {'count': 0, 'last': None, 'data': {}}
    json = read_json('./document_frequency.json', default)
    assert json.keys() == default.keys()
    return json


def write_document_frequency(obj):
    assert obj.keys() == ['count', 'last', 'data']
    return write_json('./document_frequency.json', obj)


def read_tags():
    return read_json('./tags.json', {})


def write_tags(obj):
    return write_json('./tags.json', obj)


def read_metadata():
    return read_json('./sites.json', {})


def write_metadata(obj):
    return write_json('./sites.json', obj)
