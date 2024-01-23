# link - https://www.hackerrank.com/challenges/three-month-preparation-kit-grading/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two
# HackerLand University has the following grading policy:

# Every student receives a grade in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student’s grade 
# according to these rules:

# If the difference between the grade and the next multiple of 5 is less than 3, 
# round grade up to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs as the result will still 
# be a failing grade.
# Examples

# grade = 84 round to 85 (85 – 84 is less than 3)
# grade = 29 do not round (result is less than 40)
# grade = 57 do not round (60 – 57 is 3 or higher)
# Given the initial value of grade for each of Sam’s n students, write code to automate 
# the rounding process.

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i]>37:
            if (grades[i]%5)==3:
                grades[i]=grades[i]+2
            elif grades[i]%5==4:
                grades[i]+=1
    return grades
    
    # O(n) time and O(1) space


