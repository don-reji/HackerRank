# link - https://www.hackerrank.com/challenges/three-month-preparation-kit-sparse-arrays/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one
# Problem
# There is a collection of input strings and a collection of query strings. For each query
# string, determine how many times it occurs in the list of input strings. Return an array
# of the results.

# Example:

# strings=[‘ab’, ‘ab’, ‘abc’]
# queries=[‘ab’, ‘abc’, ‘bc’]

# There are instances of ‘ab’, 1 of ‘abc’ and 0 of ‘bc’. For each query, add an element to
# the return array, results=[2,1,0].


from collections import Counter


def matchingStrings(strings, queries):
    # Write your code here

    # count the occurence of each query using counter ()
    queries_count = Counter(strings)

    result = []

    for i in queries:
        # get() gets the count of the key else 0
        result.append(queries_count.get(i, 0))
    return result
    # time and space complexity (n)
