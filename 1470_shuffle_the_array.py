"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

"""
 
def shuffle(nums, n):
    shuffled_array = [] 
    for i in range(n):
        shuffled_array.append(nums[i])
        shuffled_array.append(nums[i+n])
    return shuffled_array
print(shuffle([2,5,1,3,4,7], 3))
print(shuffle([1,2,3,4,4,3,2,1], 4))
print(shuffle([1,1,2,2], 2))