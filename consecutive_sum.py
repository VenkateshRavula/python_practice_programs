def findConsecutive(N): 
  
    start = 1
    end = 1
    sum = 1
    count = 0
      
    while start <= N/2: 
          
        if sum < N: 
            end += 1
            sum += end 
          
        if sum > N: 
            sum -= start 
            start += 1
              
        if sum == N: 
            for i in range(start, end + 1): 
                print(i, end=' ') 
            print( )
			
            count += 1 
            sum -= start  
            start += 1
    return count
# Driver code 
N = 15
print(findConsecutive(N))