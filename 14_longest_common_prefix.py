"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

>>> longestCommonPrefix(["flower", "flow", "flight"])
'fl'

>>> longestCommonPrefix(["dog", "racecar", "car"])
''

"""


def longestCommonPrefix(strs):
    if not strs:
        return ""
    rst = ""
    # * operator unwraps elements in collection type data structures. String itself can be taken as a list or collection
    # therefore "strs" is taken as two-dimension collection object here.
    for lst in zip((*strs)):
        # check all items with a list are the same, using len(set()) is a common technique
        if len(set(lst)) == 1:
            rst += lst[0]
        else:
            return rst
    return rst


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")

