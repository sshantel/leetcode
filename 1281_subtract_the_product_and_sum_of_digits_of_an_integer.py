"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.

>>> subtractProductAndSum(234)
15

>>> subtractProductAndSum(4421)
21

""" 
def subtractProductAndSum(n):
    s= str(n)
    sum=0
    product=1
    for i in range(0,len(s)):
        sum+=int(s[i])
        product*= int(s[i])
    return product-sum

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")
            