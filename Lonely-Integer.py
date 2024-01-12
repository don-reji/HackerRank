# link - https://www.hackerrank.com/challenges/three-month-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two
# Given an array of integers, where all elements but one occur twice, find the unique element.

def lonelyinteger(a):
    # Write your code here
    unique=0
    for i in a:
        unique^=i
    return unique
    # O(n) time, uses XOR
    # a number XOR itself is 0, so only the unique number remains
    
    # for i in a:
    #     if a.count(i)==1:
    #         return i
    # O(n^2) time 



