directions = set([
'north',
'south',
'east',
'west',
#'up',
#'down'
])

def scan(sentence):
    results = []
    words = sentence.split()
    for word in words:
        if word in directions:
            results.append(('direction', word))
    return results
