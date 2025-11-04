def count_digits_greater_than(n, t):
    ### Replace with your own code (begin) ###
    pass
    ### Replace with your own code (end)   ###

3) count_digits_greater_than(n, t)
   - Count how many digits of non-negative integer n are strictly greater than the digit t (0..9)
   - Return -1 if n is negative or if t is not an integer between 0 and 9



#%%


def count_digits_greater_than(n, t):
    
    if n < 0:
        return -1
    
    if not isinstance(t, int):
        return -1
    
    if t > 9 :
        return -1
    
    if t < 0 :
        return -1
        
    digits = str(n)
                 
    count = 0
                 
    for i in range (len(digits)):
        if int(digits[i]) > t:
            count += 1
            
    print("The number of non-negative digits over " + str(t) + " is:")
    
    return count
    
    

    
            

print (count_digits_greater_than(327412312908285783045723085234, 4)
       )
    