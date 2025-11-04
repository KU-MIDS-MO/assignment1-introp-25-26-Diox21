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



