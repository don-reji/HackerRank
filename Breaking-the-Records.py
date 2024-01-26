# link - https://www.hackerrank.com/challenges/three-month-preparation-kit-breaking-best-and-worst-records/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one
# Maria plays college basketball and wants to go pro. Each season she maintains a record 
# of her play. She tabulates the number of times she breaks her season record for most 
# points and least points in a game. Points scored in the first game establish her 
# record for the season, and she begins counting from there.

# Example

# scores = [12, 24, 10, 24]
# Scores are in the same order as the games played. She tabulates her results as follows:

#                                      Count
#     Game  Score  Minimum  Maximum   Min Max
#      0      12     12       12       0   0
#      1      24     12       24       0   1
#      2      10     10       24       1   1
#      3      24     10       24       1   1
# Given the scores for a season, determine the number of times Maria breaks her records 
# for most and least points scored during the season.

def breakingRecords(scores):
    # Write your code here
    count=[0,0]
    maximum=scores[0]
    minimum=scores[0]
    for i in range(1,len(scores)):
        if scores[i]>maximum:
            maximum=scores[i]
            count[0]+=1
        elif scores[i]<minimum:
            minimum=scores[i]
            count[1]+=1
    return count
    # O(n) time and O(1) space  