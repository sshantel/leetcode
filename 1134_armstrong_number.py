
def isArmstrong(N):
    k = len(str(N)) 
    sum = 0
    for digit in str(N):
        power = pow(int(digit), k) 
        sum += power 
    
    if sum == N:
        return True 


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** YAY! GIVEN TESTS PASSED.\n")