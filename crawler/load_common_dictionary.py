from requests import get
import json


def get_list():
    res = get('https://norvig.com/ngrams/count_1w.txt')
    text = res.content.decode('utf-8').split('\n')
    text = [tuple(l.split('\t')) for l in text if len(l) > 0]
    text = [(k, int(v)) for k, v in text]
    return text


def build_dict(text):
    s = sum([v for k, v in text])
    text = text[:5000]  # 5k (altho below filter will only return ~3k)
    return {t: round(v / s, 4) for t, v in text if round(v / s, 4) > 0}


def save_dict():
    l = get_list()
    d = build_dict(l)
    with open('./english_freq.json', 'w') as outfile:
        json.dump(d, outfile)


if __name__ == '__main__':
    save_dict()
