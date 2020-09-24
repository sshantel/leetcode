"""
Given two integer arrays of equal length target and arr.

In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.

Return True if you can make arr equal to target, or False otherwise.

"""

def canBeEqual(target, arr):
    mp = dict()
    for x in arr:
        if x in mp.keys():
            mp[x]+=1
        else:
            mp[x] = 1
    for x in target:
        if x in mp.keys():
            mp[x]-=1
    for x in mp:
        if mp[x]!=0:
            return False
    return True
print(canBeEqual([1,2,3,4], [2,4,1,3]))
print(canBeEqual([7], [7]))
print(canBeEqual([1,12], [12,1]))