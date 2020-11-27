"""
The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.

Given a positive integer N, return true if and only if it is an Armstrong number.

<<< isArmstrong(153)
True

<<< isArmstrong(123)
False

"""
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