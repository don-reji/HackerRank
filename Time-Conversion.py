# link - https://www.hackerrank.com/challenges/three-month-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one
# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

# Note: – 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# – 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Example

# s = ’12:01:00PM’
# Return ’12:01:00′.
# s = ’12:01:00AM’
# Return ’00:01:00′.


def timeConversion(s):
    # Write your code here
    if s[-2:]=='AM':
        if s[:2]=='12':
            return '00'+s[2:-2]
        else:
            return s[:-2]
    else:
        if int(s[:2])<12:
            return str(int(s[:2])+12)+s[2:-2]
        else:
            return s[:-2]
            
    # O(1) time and space
