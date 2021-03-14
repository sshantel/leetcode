"""
Given an integer n and an array a of length n, your task is to apply the following mutation to a:

Array a mutates into a new array b of length n.
For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0. For example, b[0] should be equal to 0 + a[0] + a[1].
Example

For n = 5 and a = [4, 0, 1, -2, 3], the output should be mutateTheArray(n, a) = [4, 5, -1, 2, 1].

b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1
So, the resulting array after the mutation will be [4, 5, -1, 2, 1].

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

An integer representing the length of the given array.

Guaranteed constraints:
1 ≤ n ≤ 103.

[input] array.integer a

An array of integers that needs to be mutated.

Guaranteed constraints:
a.length = n,
-103 ≤ a[i] ≤ 103.

[output] array.integer

The resulting array after the mutation

n: 5
a: [4, 0, 1, -2, 3]
Expected Output:
[4, 5, -1, 2, 1]


Input:
n: 1
a: [9]
Expected Output:
[9]


Input:
n: 4
a: [1, 2, 3, 4]
Expected Output:
[3, 6, 9, 7]

Input:
n: 9
a: [-9, -8, 7, 7, 7, 6, -6, 4, 6]
Expected Output:
[-17, -10, 6, 21, 20, 7, 4, 4, 10]

Input:
n: 10
a: [6, -5, -5, 5, 10, 5, 1, 8, 6, -2]
Expected Output:
[1, -4, -5, 10, 20, 16, 14, 15, 12, 4]

Input:
n: 10
a: [1, 10, 10, -6, 5, -3, -7, 10, 9, 10]
Expected Output:
[11, 21, 14, 9, -4, -5, 0, 12, 29, 19]

Input:
n: 4
a: [-6, -5, -7, -1]
Expected Output:
[-11, -18, -13, -8]

Input:
n: 8
a: [-4, -5, 0, -6, -5, -4, -7, 9]
Expected Output:
[-9, -9, -11, -11, -15, -16, -2, 2]

Input:
n: 1
a: [-5]
Expected Output:
[-5]

Input:
n: 5
a: [-9, -6, 10, -6, -10]
Expected Output:
[-15, -5, -2, -6, -16]
"""

def mutateTheArray(n, a):
    array_b = []
    
    for i in range(n):
        if i == 0:
            b = 0 + a[i] + a[i + 1]
            array_b.append(b)
        
        elif i >= n-1:
            b = a[i - 1] + a[i] + 0
            array_b.append(b)
            
        else:
            b = a[i - 1] + a[i] + a[i + 1]
            array_b.append(b)
            
    return array_b