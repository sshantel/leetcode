"""
Given a sentence that consists of some words separated by a single space, and a searchWord.

You have to check if searchWord is a prefix of any word in sentence.

Return the index of the word in sentence where searchWord is a prefix of this word (1-indexed).

If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

A prefix of a string S is any leading contiguous substring of S.

>>> isPrefixOfWord("i love eating burger", "burg")
4

>>> isPrefixOfWord("this problem is an easy problem", "pro")
2
"""

def isPrefixOfWord(sentence, searchWord):
    sentence_split = sentence.split()  
    for i in range(1, len(sentence_split) + 1):
        if sentence_split[i].startswith(searchWord):
            i += 1
            return i
    else:
        return -1

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')