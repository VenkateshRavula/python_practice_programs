
def perfect_number(num):
  i=1; sum=0;
  while i <= num/2:
    if num % i == 0:
        print(i)
        sum += i
    i += 1

  if sum == num:
    print("%d is perfect number" %num)
  else:
    print("%d is not perfect number" %num)


num = input("enter a number: ")
perfect_number(num)
