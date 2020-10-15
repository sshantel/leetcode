"""
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
>>>arrayRankTransform([40,10,20,30])
[4,1,2,3]
>>>arrayRankTransform([100,100,100])
[1,1,1]
arrayRankTransform([37,12,28,9,100,56,80,5,12])
[5,3,4,2,8,6,7,1,3]
"""

def arrayRankTransform(arr):
    d={}
    res=[]
    rnk=1
    for x in sorted(arr):
        if x not in d:
            d[x] = rnk
            rnk +=1
        else:
            d[x] = rnk-1
    print(d)
    for i in arr:
        res.append(d[i])
    return res
    
if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")