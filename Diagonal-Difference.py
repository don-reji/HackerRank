# link - https://www.hackerrank.com/challenges/three-month-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix arr is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  

# The left-to-right diagonal = 1 + 5 +9 = 15. The right to left diagonal = 3 + 5 + 9 = 17. 
# Their absolute difference is |15 – 17| = 2.


def diagonalDifference(arr):
    # Write your code here
    n=len(arr[0])
    right=0
    left=0
    for i in range(n):
        right+=arr[i][i]
        left+=arr[i][n-1-i]
    return abs(right-left)
    # O(n) time and O(1) space