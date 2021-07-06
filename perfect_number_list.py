n = input("Enter the number: ")

def perfect_number(n):
    i=1; sum=0
    while i <= n/2:
        if n%i == 0:
            sum += i
        i += 1
    if sum == n:
        return True
    else:
        return False

for num in range(1, n+1):
    result = perfect_number(num)
    if result is True:
        print num