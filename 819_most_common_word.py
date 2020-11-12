"""
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

>>> mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ['hit'])
'ball'

"""

def mostCommonWord(paragraph, banned):
    paragraph = paragraph.replace(',', ' ')
    paragraph = paragraph.replace('  ', ' ')
    d =  {}
    words = paragraph.split(' ')
    for word in words:
        word = word.replace('.', '')
        word = word.replace(',', '')
        word = word.replace('?', '')
        word = word.replace('!', '')
        word = word.replace(';', '')
        word = word.replace(':', '')
        word = word.replace("'", '')
        word = word.lower()
        if word in d: 
            d[word] += 1
        else: 
            d[word] = 1
        
    m = 0
    w = ''
    for k in d:
        if k not in banned and d[k] > m:
            m = d[k]
            w = k
    return w


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')