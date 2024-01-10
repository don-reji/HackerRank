# A left rotation operation on an array of size  shifts each of the array's elements  
# unit to the left. Given an integer, , rotate the array that many steps left and return
# the result

# solution

def rotateLeft(d, arr):
    # Write your code here
    
    # implementation 1
    def reverse(arr,start,end):
        while start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
    # Reverse the elements from the start to d-1
    reverse(arr, 0, d - 1)
    # Reverse the elements from d to n-1
    reverse(arr, d, n - 1)
    # Reverse the entire array
    reverse(arr, 0, n - 1)
    return arr
    # O(n) time and O(1) space 
    
    
    # implemenation 2
    return arr[d:]+arr[:d]
# O(n) space. O(n) time since concatenation creates new variable