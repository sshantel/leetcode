"""
Given an integer n, return any array containing n unique integers such that they add up to 0.

"""

def sumZero(n: int):
    a=[]
    if n%2!=0:
        a.append(0)
    for i in range(1,n):
        if len(a)==n:
            break
        a.append(i)
        a.append(-i)
    return a
print(sumZero(5))
print(sumZero(3))
print(sumZero(1))