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
    
    return count
    
    

    
            

