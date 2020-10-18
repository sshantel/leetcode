"""
Given an array of string words. Return all strings in words which is substring of another word in any order. 

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

>>> stringMatching(["mass","as","hero","superhero"])
['as', 'hero']

>>> stringMatching(["leetcode","et","code"])
['et', 'code']

>>> stringMatching["blue","green","bu"]
[]

"""

def stringMatching(words):
    l = []
    for i in words:
        for j in words:
            if j in i and j!= i:
                if j not in l:
                    l.append(j)
    return l

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
