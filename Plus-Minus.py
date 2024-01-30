# link - https://www.hackerrank.com/challenges/three-month-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one

# Given an array of integers, calculate the ratios of its elements that are positive, 
# negative, and zero. Print the decimal value of each fraction on a new line with 6 places
# after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal 
# places, though answers with absolute error of up to 10-4 are acceptable.

# Example

# arr = [1, 1, 0, -1, -1]
# There are n = 5 elements, two positive, two negative and one zero. Their ratios are 
# 2/5 = 0.400000, 2/5 = 0.400000 and 1/5 = 0.200000. Results are printed as:

# 0.400000
# 0.400000
# 0.200000

def plusMinus(arr):
    # Write your code here
    positive,negative,zero=0,0,0
    for i in arr:
        if i >0:
            positive+=1
        elif i<0:
            negative+=1
        else:
            zero+=1
    n=len(arr)
    print(round(positive/n,6))
    print(round(negative/n,6))
    print(round(zero/n,6))
    
    # O(n) time