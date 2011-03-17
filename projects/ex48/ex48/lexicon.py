categories = {
    'direction': set([
        'north',
        'south',
        'east',
        'west',
        'up',
        'down',
        ]),
    'verb': set([
        'go',
        'kill',
        'eat',
        ]),
    'stop': set([
        'the',
        'in',
        'of',
        ]),
    'noun': set([
        'bear',
        'princess',
        ]),
}

def convert_word(word):
    # Check each category
    for category_name in categories.keys():
        if word in categories[category_name]:
            return((category_name, word))
    return None

def convert_number(string):
    try:
        return int(string)
    except ValueError:
        return None

def scan(sentence):
    results = []
    words = sentence.split()
    for word in words:
        # Is this a word?
        result = convert_word(word)
        if result != None:
            results.append(result)
            continue
        # Is this a number?
        result = convert_number(word)
        if result != None:
            results.append(('number', result))
            continue
        # Error.
        results.append(('error', word))
    return results
