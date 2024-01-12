# link - https://www.hackerrank.com/challenges/three-month-preparation-kit-caesar-cipher-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-four
# Julius Caesar protected his confidential information by encrypting it using a cipher. 
# Caesar’s cipher shifts each letter by a number of letters. If the shift takes you past 
# the end of the alphabet, just rotate back to the front of the alphabet. In the case of a 
# rotation by 3, w, x, y and z would map to z, a, b and c.

# Example

# s = There’s-a-starman-waiting-in-the-sky
# k = 3

# The alphabet is rotated by 3, matching the mapping above. The encrypted string is 
# Wkhuh’v-d-vwdupqd-zdlwlqj-lq-wkh-vnb.

# Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

# Function Description

# Complete the caesarCipher function in the editor below.

# caesarCipher has the following parameter(s):

# string s: cleartext
# int k: the alphabet rotation factor
# Returns

# string: the encrypted string
# Input Format
# The first line contains the integer, n, the length of the unencrypted string.
# The second line contains the unencrypted string, s.
# The third line contains k, the number of letters to rotate the alphabet by.

# Constraints
# 1 <= n <= 100
# 0 <= k <= 100
# s is a valid ASCII string without any spaces.

import string
def caesarCipher(s: str, k: int) -> str:
    symbols_low = string.ascii_lowercase
    symbols_up = string.ascii_uppercase
    res = ''
    for c in s:
        if c.isupper():
            res+=symbols_up[(symbols_up.index(c)+k)%len(symbols_up)]
        elif c.islower():
            res+=symbols_low[(symbols_low.index(c)+k)%len(symbols_low)]
        else:
            res+=c
                       
    return res
# O(n) time and space complexity