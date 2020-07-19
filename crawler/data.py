import json


def read_sites():
    with open('../discovery/sites.txt') as f:
        data = f.read().split('\n')
        f.close()
        return data


def write_sites(data):
    with open('../discovery/sites.txt', 'w') as f:
        f.write(data)
        f.close()


def read_json(file, default=None):
    try:
        with open(file) as infile:
            return json.load(infile)
    except FileNotFoundError as e:
        return default


def write_json(file, obj):
    with open(file, 'w') as outfile:
        json.dump(obj, outfile)
