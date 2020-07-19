
def read_sites():
    with open('../discovery/sites.txt') as f:
        data = f.read().split('\n')
        f.close()
        return data


def write_sites(data):
    with open('../discovery/sites.txt', 'w') as f:
        f.write(data)
        f.close()