def sum_of_cubes_even(n):
    ### Replace with your own code (begin) ###
    pass
    ### Replace with your own code (end)   ###


2) sum_of_cubes_even(n)
   - Return the sum of cubes of all even numbers from 0 up to and including n, as a float
   - Return -1 if n is negative or not an integer
   - If n > 2000, print a warning but still compute
   
#%%

def sum_of_cubes_even(n):
    
    total = 0
    
    for num in range(0, n + 1):
        if num % 2 == 0 :
            total += num ** 3

    if n < 0 or not isinstance(n, int):
        return -1

    if total > 2000:
        print("WARNING, > 2000")
        
        
    return float(total)



print (sum_of_cubes_even(35))

