

 
def findKthPositive(arr, k):
    s=set(arr)
    count=0
    i=1
    while True:
        if i not in s:
            count+=1
            if count==k:
                return i
        i=i+1 
print(findKthPositive[2,3,4,7,11], 5)
print(findKthPositive[1,2,3,4], 2)