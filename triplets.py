l = [1,2,3,4,5,6,7,8,9,10]

def sum(a,b,c):
    sum = a + b + c
    if sum == 10:
        return True
    else:
        return False

filter(sum, l)
