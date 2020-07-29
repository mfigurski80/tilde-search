# source from https://github.com/jedijulia/porter-stemmer/blob/master/stemmer.py
# the original version has been altered to be functional

def _isCons(letter):
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        return False
    else:
        return True


def _isConsonant(word, i):
    letter = word[i]
    if _isCons(letter):
        if letter == 'y' and _isCons(word[i-1]):
            return False
        else:
            return True
    else:
        return False


def _isVowel(word, i):
    return not(_isConsonant(word, i))

# *S


def _endsWith(stem, letter):
    if stem.endswith(letter):
        return True
    else:
        return False

# *v*


def _containsVowel(stem):
    for i in stem:
        if not _isCons(i):
            return True
    return False

# *d


def _doubleCons(stem):
    if len(stem) >= 2:
        if _isConsonant(stem, -1) and _isConsonant(stem, -2):
            return True
        else:
            return False
    else:
        return False


def _getForm(word):
    form = []
    formStr = ''
    for i in range(len(word)):
        if _isConsonant(word, i):
            if i != 0:
                prev = form[-1]
                if prev != 'C':
                    form.append('C')
            else:
                form.append('C')
        else:
            if i != 0:
                prev = form[-1]
                if prev != 'V':
                    form.append('V')
            else:
                form.append('V')
    for j in form:
        formStr += j
    return formStr


def _getM(word):
    form = _getForm(word)
    m = form.count('VC')
    return m

# *o


def _cvc(word):
    if len(word) >= 3:
        f = -3
        s = -2
        t = -1
        third = word[t]
        if _isConsonant(word, f) and _isVowel(word, s) and _isConsonant(word, t):
            if third != 'w' and third != 'x' and third != 'y':
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def _replace(orig, rem, rep):
    result = orig.rfind(rem)
    base = orig[:result]
    replaced = base + rep
    return replaced


def _replaceM0(orig, rem, rep):
    result = orig.rfind(rem)
    base = orig[:result]
    if _getM(base) > 0:
        replaced = base + rep
        return replaced
    else:
        return orig


def _replaceM1(orig, rem, rep):
    result = orig.rfind(rem)
    base = orig[:result]
    if _getM(base) > 1:
        replaced = base + rep
        return replaced
    else:
        return orig


def _step1a(word):
    if word.endswith('sses'):
        word = _replace(word, 'sses', 'ss')
    elif word.endswith('ies'):
        word = _replace(word, 'ies', 'i')
    elif word.endswith('ss'):
        word = _replace(word, 'ss', 'ss')
    elif word.endswith('s'):
        word = _replace(word, 's', '')
    else:
        pass
    return word


def _step1b(word):
    flag = False
    if word.endswith('eed'):
        result = word.rfind('eed')
        base = word[:result]
        if _getM(base) > 0:
            word = base
            word += 'ee'
    elif word.endswith('ed'):
        result = word.rfind('ed')
        base = word[:result]
        if _containsVowel(base):
            word = base
            flag = True
    elif word.endswith('ing'):
        result = word.rfind('ing')
        base = word[:result]
        if _containsVowel(base):
            word = base
            flag = True
    if flag:
        if word.endswith('at') or word.endswith('bl') or word.endswith('iz'):
            word += 'e'
        elif _doubleCons(word) and not _endsWith(word, 'l') and not _endsWith(word, 's') and not _endsWith(word, 'z'):
            word = word[:-1]
        elif _getM(word) == 1 and _cvc(word):
            word += 'e'
        else:
            pass
    else:
        pass
    return word


def _step1c(word):
    if word.endswith('y'):
        result = word.rfind('y')
        base = word[:result]
        if _containsVowel(base):
            word = base
            word += 'i'
    return word


def _step2(word):
    if word.endswith('ational'):
        word = _replaceM0(word, 'ational', 'ate')
    elif word.endswith('tional'):
        word = _replaceM0(word, 'tional', 'tion')
    elif word.endswith('enci'):
        word = _replaceM0(word, 'enci', 'ence')
    elif word.endswith('anci'):
        word = _replaceM0(word, 'anci', 'ance')
    elif word.endswith('izer'):
        word = _replaceM0(word, 'izer', 'ize')
    elif word.endswith('abli'):
        word = _replaceM0(word, 'abli', 'able')
    elif word.endswith('alli'):
        word = _replaceM0(word, 'alli', 'al')
    elif word.endswith('entli'):
        word = _replaceM0(word, 'entli', 'ent')
    elif word.endswith('eli'):
        word = _replaceM0(word, 'eli', 'e')
    elif word.endswith('ousli'):
        word = _replaceM0(word, 'ousli', 'ous')
    elif word.endswith('ization'):
        word = _replaceM0(word, 'ization', 'ize')
    elif word.endswith('ation'):
        word = _replaceM0(word, 'ation', 'ate')
    elif word.endswith('ator'):
        word = _replaceM0(word, 'ator', 'ate')
    elif word.endswith('alism'):
        word = _replaceM0(word, 'alism', 'al')
    elif word.endswith('iveness'):
        word = _replaceM0(word, 'iveness', 'ive')
    elif word.endswith('fulness'):
        word = _replaceM0(word, 'fulness', 'ful')
    elif word.endswith('ousness'):
        word = _replaceM0(word, 'ousness', 'ous')
    elif word.endswith('aliti'):
        word = _replaceM0(word, 'aliti', 'al')
    elif word.endswith('iviti'):
        word = _replaceM0(word, 'iviti', 'ive')
    elif word.endswith('biliti'):
        word = _replaceM0(word, 'biliti', 'ble')
    return word


def _step3(word):
    if word.endswith('icate'):
        word = _replaceM0(word, 'icate', 'ic')
    elif word.endswith('ative'):
        word = _replaceM0(word, 'ative', '')
    elif word.endswith('alize'):
        word = _replaceM0(word, 'alize', 'al')
    elif word.endswith('iciti'):
        word = _replaceM0(word, 'iciti', 'ic')
    elif word.endswith('ful'):
        word = _replaceM0(word, 'ful', '')
    elif word.endswith('ness'):
        word = _replaceM0(word, 'ness', '')
    return word


def _step4(word):
    if word.endswith('al'):
        word = _replaceM1(word, 'al', '')
    elif word.endswith('ance'):
        word = _replaceM1(word, 'ance', '')
    elif word.endswith('ence'):
        word = _replaceM1(word, 'ence', '')
    elif word.endswith('er'):
        word = _replaceM1(word, 'er', '')
    elif word.endswith('ic'):
        word = _replaceM1(word, 'ic', '')
    elif word.endswith('able'):
        word = _replaceM1(word, 'able', '')
    elif word.endswith('ible'):
        word = _replaceM1(word, 'ible', '')
    elif word.endswith('ant'):
        word = _replaceM1(word, 'ant', '')
    elif word.endswith('ement'):
        word = _replaceM1(word, 'ement', '')
    elif word.endswith('ment'):
        word = _replaceM1(word, 'ment', '')
    elif word.endswith('ent'):
        word = _replaceM1(word, 'ent', '')
    elif word.endswith('ou'):
        word = _replaceM1(word, 'ou', '')
    elif word.endswith('ism'):
        word = _replaceM1(word, 'ism', '')
    elif word.endswith('ate'):
        word = _replaceM1(word, 'ate', '')
    elif word.endswith('iti'):
        word = _replaceM1(word, 'iti', '')
    elif word.endswith('ous'):
        word = _replaceM1(word, 'ous', '')
    elif word.endswith('ive'):
        word = _replaceM1(word, 'ive', '')
    elif word.endswith('ize'):
        word = _replaceM1(word, 'ize', '')
    elif word.endswith('ion'):
        result = word.rfind('ion')
        base = word[:result]
        if _getM(base) > 1 and (_endsWith(base, 's') or _endsWith(base, 't')):
            word = base
        word = _replaceM1(word, '', '')
    return word


def _step5a(word):
    if word.endswith('e'):
        base = word[:-1]
        if _getM(base) > 1:
            word = base
        elif _getM(base) == 1 and not _cvc(base):
            word = base
    return word


def _step5b(word):
    if _getM(word) > 1 and _doubleCons(word) and _endsWith(word, 'l'):
        word = word[:-1]
    return word


def stem(word):
    """ Runs Porter stemming algorithm on given word
    Usage:
    >>> stem('running')
    'run'
    """
    try:
        word = _step1a(word)
        word = _step1b(word)
        word = _step1c(word)
        word = _step2(word)
        word = _step3(word)
        word = _step4(word)
        word = _step5a(word)
        word = _step5b(word)
        return word
    except:
        return word


if __name__ == '__main__':
    print(stem('running'))
