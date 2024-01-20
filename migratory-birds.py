# link - https://www.hackerrank.com/challenges/three-month-preparation-kit-migratory-birds/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-three
# Given an array of bird sightings where every element represents a bird type id, 
# determine the id of the most frequently sighted type. If more than 1 type has been 
# spotted that maximum amount, return the smallest of their ids.

# Example
# arr = [1, 1, 2, 2, 3]
# There are two each of types 1 and 2, and one sighting of type 3. Pick the lower of the 
# two types seen twice: type 1.


from collections import Counter
def migratoryBirds(arr):
    # Write your code here
    
    # solution 1

    # Count the occurrences of each bird type using Counter
    bird_counts=Counter(arr)
    # get max count
    max_count=max(bird_counts.values())
    # get min id with max count
    min_id=min(key for key,value in bird_counts.items() if value==max_count)
    return min_id
    # O(n) space and time
        
    # solution 2

    # max_sight=arr.count(arr[0])
    # max_id=arr[0]
    # for i in set(arr):
    #     if arr.count(i)>max_sight:
    #         max_sight=arr.count(i)
    #         max_id=i
    #     elif arr.count(i)==max_sight:
    #         max_id=min(i,max_id)
    # return max_id
    # # O(n^2) time and O(1) space 