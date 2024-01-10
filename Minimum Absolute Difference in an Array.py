# The absolute difference is the positive difference between two values 𝑎 and 𝑏, is
# written |𝑎 − 𝑏| or |𝑏 − 𝑎| and they are equal. If 𝑎 = 3 and 𝑏 = 2,
# |3 − 2| = |2 − 3| = 1. Given an array of integers, find the minimum absolute
# difference between any two elements in the array.
# Example: arr = [−2, 2,4]
# There are three pairs of numbers: [−2, 2], [−2,4] and [𝟐 ,𝟒]. The absolute 
# differences for these pairs are  |(−𝟐) − 𝟐 | =4 ,|(−𝟐) −4 |=6 and 
# |𝟐 −4 |=𝟐 .The minimum absolute difference is 𝟐.

def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff=abs(arr[0]-arr[1])
    for i in range(1,len(arr)-1):
        now=abs(arr[i]-arr[i+1])
        if now < min_diff:
            min_diff=now
    return min_diff

# O(nlog n) time and O(1) space complexity
# sorting the array first gets the numbers with minimum differences to each other
