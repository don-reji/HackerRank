# link - https://www.hackerrank.com/challenges/three-month-preparation-kit-divisible-sum-pairs/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one
# Given an array of integers and a positive integer k, determine the number of (i, j) 
# pairs where i < j and ar[i] + ar[j] is divisible by k.

# Example

# ar = [1, 2, 3, 4, 5, 6]
# k = 5
# Three pairs meet the criteria: [1, 4], [2, 3], and [4, 6].

# Function Description

# Complete the divisibleSumPairs function in the editor below.

# divisibleSumPairs has the following parameter(s):

# int n: the length of array ar 
# int ar[n]: an array of integers
# int k: the integer divisor
# Returns
# int: the number of pairs



def divisibleSumPairs(n, k, ar):
    # Write your code here
    pairs=0
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            if (ar[i]+ar[j]) % k==0 :
                pairs+=1
    return pairs
    # O(n^2) time and O(1) space 