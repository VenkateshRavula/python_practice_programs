N = int(input("enter a range: "))

def findDivisibleBy3(N):
    for num in range(N+1, 3, -1):
        print(num)