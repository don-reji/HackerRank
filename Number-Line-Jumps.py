# In this Number Line Jumps problem, you are given two kangaroos on a number line ready 
# to jump in the positive direction (i.e, toward positive infinity). The first kangaroo 
# starts at location x1 and moves at a rate of v1 meters per jump. The second kangaroo 
# starts at location x2 and moves at a rate of v2 meters per jump. You have to figure out
# a way to get both kangaroos at the same location at the same time as part of the show. 
# If it is possible, return YES, otherwise return NO.

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1<x2 and v1 < v2:
        return 'NO'
    # if 1st kangaroo starts at a lower location and lower 
    # jump rate it won't catch upto 2nd
    
    else:
        if v1!=v2 and (x2-x1)%(v2-v1)==0:
    # if jump rate is same it never will be at same location
    # 
            return 'YES'      
        else:
            return 'NO'
            
    # O(1) time
    
    # for i in range(10000):
    #     if x1==x2: 
    #         return 'YES'
    #     else:
    #         x1+=v1
    #         x2+=v2
    # return 'NO'
    # O(n) time 



