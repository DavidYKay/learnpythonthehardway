directions = set([
'north',
'south',
'east',
'west',
'up',
'down',
])

verbs = set([
'go',
'kill',
'eat',
])

categories = {
    'direction': directions,
    'verb': verbs,
}

def scan(sentence):
    results = []
    words = sentence.split()
    for word in words:
        # Check each category
        #for category_name, category_words in categories:
        for category_name in categories.keys():
            category_words = categories[category_name]
            if word in category_words:
                results.append((category_name, word))
    return results
