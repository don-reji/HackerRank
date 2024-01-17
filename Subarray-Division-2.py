# link - https://www.hackerrank.com/challenges/three-month-preparation-kit-the-birthday-bar/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-three
# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an 
# integer on it.
# Lily decides to share a contiguous segment of the bar selected such that:
# The length of the segment matches Ron's birth month, and,
# The sum of the integers on the squares is equal to his birth day.
# Determine how many ways she can divide the chocolate.


def birthday(s, d, m):
    # Write your code here
    result=0
    for i in range(len(s)):
        if sum(s[i:i+m])==d:
            result+=1
    return result

# O(N) time and O(1) space