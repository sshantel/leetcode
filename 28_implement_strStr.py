"""

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

"""

def strStr(haystack, needle)

    if needle not in haystack:
        return -1
    elif len(haystack) == 0 or len(needle) ==0:
        return 0
    else:
        return haystack.index(needle)
print(strStr("hello", "ll"))
print(strStr("aaaaa", "bba"))