#directions = 
#set([
#'north',
#'south',
#'east',
#'west',
#'up',
#'down',
#])

verbs = set([
'go',
'kill',
'eat',
])

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
}

def scan(sentence):
    results = []
    words = sentence.split()
    for word in words:
        # Check each category
        for category_name in categories.keys():
            if word in categories[category_name]:
                results.append((category_name, word))
    return results
