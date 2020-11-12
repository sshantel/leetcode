"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)


>>> lastStoneWeight([2, 7, 4, 1, 8, 1])
1

"""



def lastStoneWeight(stones):
    while len(stones) > 1: 
        x = stones.pop(stones.index(max(stones)))   
        y = stones.pop(stones.index(max(stones)))
        if x != y:
            stones.append(abs(y - x))
    return stones[0] if len(stones) == 1 else 0


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')