"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

<<< shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'practice')
3

<<< shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'practice')
3 

"""


def shortestDistance(words, word1, word2):

    idx1 = -len(words)
    idx2 = -len(words)
    distance = len(words)

    for idx, word in enumerate(words):
        if word == word1:
            idx1 = idx
            distance = min(distance, idx - idx2)
        elif word == word2:
            idx2 = idx
            distance = min(distance, idx - idx1)

    return distance


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n✨ ALL TESTS PASSED!\n")

