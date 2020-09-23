"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.
"""

 def repeatedNTimes(A):
    seen = set()
    for num in A:
        if num in seen:
            return num
        seen.add(num)

