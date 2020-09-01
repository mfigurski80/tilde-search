from firebase import firebase
import json

URL = 'https://tilde-search.firebaseio.com/'
fb = firebase.FirebaseApplication(URL, None)


def encode_for_firebase(text):
    return ''.join(f'%{ord(c)}%' if not 64 < ord(c) < 122 else c for c in text)


def encode_keys(d):
    return {encode_for_firebase(k): v for k, v in d.items()}


def print_progress(percent):
    count = round(percent * 20)
    print(f'{count * "█"}{(20-count) * "_"} [%{round(percent*100)}]', end='\r')
    if count == 20:
        print()


data = json.load(open('../data/tags.json'))

print('Cleaning data...')
data = encode_keys(data)
for i, tag in enumerate(data):
    print_progress(i/len(data))
    data[tag] = encode_keys(data[tag])

print('Uploading data...')
for i, tag in enumerate(data):
    print_progress(i/len(data))
    result = fb.put('/search', tag, data[tag])

print('Done')
