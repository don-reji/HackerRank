# Sorting is useful as the first step in many different tasks. 
# The most common task is to make finding things easier, but there are other uses as well. 
# In this case, it will make it easier to determine which pair or pairs of elements have 
# the smallest absolute difference between them.
# Example
# arr = [5, 2, 3, 4, 1]
# Sorted array is as follows sorted_arr = [1, 2, 3, 4, 5] . 
# Then we find the pairs with minimum difference such as (1, 2), (2, 3), (3, 4) and (4,5). 
# Finally, we return the array: [1, 2, 2, 3, 3, 4, 4, 5]

# Solution
def closestNumbers(arr):
    # Write your code here
    # 1
    arr.sort()
    # 2
    min_diff=arr[1]-arr[0]
    result=[]
    for i in range (2,len(arr)-1):
        min_diff=min(min_diff,arr[i+1]-arr[i])
    #  3 
    for i in range(len(arr)-1):
        if arr[i+1]-arr[i]==min_diff:
            result.append(arr[i])
            result.append(arr[i+1])
    return result
        
# O(nlogn) time cuz of sorting and looping, space O(1)
# 1.sort the array
# 2. finding the minimum difference among the array
# 3. add only the pair of numbers with the min diff into result 