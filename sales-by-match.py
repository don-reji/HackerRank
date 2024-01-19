# link - https://www.hackerrank.com/challenges/three-month-preparation-kit-sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-three

# There is a large pile of socks that must be paired by color. Given an array of integers 
# representing the color of each sock, determine how many pairs of socks with matching colors 
# there are.

# Example

# n = 7
# ar = [1, 2, 1, 2, 1, 3, 2]
# There is one pair of color 1 and one of color 2. There are three odd socks left, one of 
# each color. The number of pairs is 2.

def sockMerchant(n, ar):
    # Write your code here
    
    # solution 1

    # dictionary for keeping count of each color
    dic={}
    # Iterate through the array and count occurrences of each color
    for i in ar:
        if i not in dic:
            dic[i]=1
        elif i in dic:
            dic[i]+=1
    # Calculate the number of pairs for each color and sum them up
    res=sum(count//2 for count in dic.values())
    return res
    # O(n) space and time 
    
    # # solution 2
    
    # res =0
    # for i in set(ar):
    #     res+=ar.count(i)//2
    # return res
    # # O(n^2) time and O(n) space 