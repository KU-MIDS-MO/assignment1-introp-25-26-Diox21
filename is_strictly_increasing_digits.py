def is_strictly_increasing_digits(n):
    ### Replace with your own code (begin) ###
    pass
    ### Replace with your own code (end)   ###


#1) is_strictly_increasing_digits(n)
   - #Return True if the digits of a non-negative integer n are strictly increasing from left to right
   - #Return False otherwise
   - #Return -1 if n is negative or not an intiger
   
#%%

def is_strictly_increasing_digits(n):

#Checking here if n is negative
    if n < 0:
        return -1
#checking here if n is an integer or not
    if not isinstance(n, int):
        return -1
#here converting n to a string to see digits 
    digits = str(n)
#here single digit numbers are obviously increasing 
    if len(digits) == 1:
        return True 
#here we are saying if the previous number is greater than or equal to the next then it shall return false, if not then true. 
    for i in range (len(digits) -1):
        if digits[i] >= digits[i + 1]:
            return False    
        
    return True
    

   
   