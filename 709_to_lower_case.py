"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

>>> 'Hello'
'hello'

>>> 'here'
'here'

>>> 'LOVELY'
'lovely'


"""
def toLowerCase(str):
    return str.lower()
print(toLowerCase('Hello'))

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")