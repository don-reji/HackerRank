# link - https://www.hackerrank.com/challenges/three-month-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one
# Given five positive integers, find the minimum and maximum values that can be calculated 
# by summing exactly four of the five integers. Then print the respective minimum and 
# maximum values as a single line of two space-separated long integers.

# Example

# arr = [1, 3, 5, 7, 9]
# The minimum sum is 1 + 3 +5 +7 = 16 and the maximum sum is 3 + 5 + 7 + 9 = 24. 
# The function prints

# 16 24


def miniMaxSum(arr)->str:
    # Write your code here
    total_sum=sum(arr)
    mini=total_sum-max(arr)
    maxi=total_sum-min(arr)
    return print(mini,maxi)
    # O(n) time
    
    # arr.sort()
    # return print(sum(arr[:-1]), sum(arr[1:]))
    #  O(nlogn) time 