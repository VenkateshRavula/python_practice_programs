def CountWays(n,k): 
  
    # table[i] will be storing the number of 
    # solutions for value i. We need n+1 rows 
    # as the table is consturcted in bottom up 
    # manner using the base case (n = 0) 
    # Initialize all table values as 0 
    table =[0] * (n + 1) 
  
    # Base case (If given value is 0) 
    # Only 1 way to get 0 (select no integer) 
    table[0] = 1
  
    # Pick all integer one by one and update the 
    # table[] values after the index greater 
    # than or equal to n 
    for i in range(1, n ): 
  
        for j in range(i , k + 1):
            table[i] +=  table[i - j]             
  
    return table[n]

print(CountWays(9,3))