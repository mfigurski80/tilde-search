from Porter import stem


def get_stop_words():
    with open('./stopwords.txt') as f:
        data = f.read().split('\n')
        f.close()
        return data


stop_words = get_stop_words()
stop_chars = [',', '.', '!', '?', ':', ';', '\'', '"']
stem_seqs = ['e', 'es', 'ing', 'ed', 'ly']


def clean_word(word):
    """ Cleans useless chars from words
    Usage:
    >>> clean_word('Hemingway\\'s ')
    'hemingways'
    """
    for c in stop_chars:
        word = word.replace(c, '')
    return word.strip().lower()


def tokenize(corpus):
    """ Convert words into stemmed and cleaned tokens
    Usage:
    >>> tokenize('Let\\'s go running')
    ['let', 'go', 'run']
    """
    words = corpus.split(' ')
    words = [stem(clean_word(word)) for word in words if word not in stop_words]
    return words


if __name__ == '__main__':
    text = 'My grandma loves the cookie\'s taste so much, she\'ll bake us some more!'
    tokens = tokenize(text)
    print(f'{text}\n{" ".join(tokens)}')
