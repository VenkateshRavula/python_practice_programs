# decorator
def star(func):
    def inner(*args):
        if args[0] < 2:
            print "Whoops! minium input value should be 2"
            return
        print("*" * 20)
        func(*args)
        print("*" * 20)

    return inner

# decorator
def equals(func):
    def inner(*args):
        print("=" * 25)
        func(*args)
        print("=" * 20)
    return inner


# Common Function
@star
@equals
def prime(num):
    for i in range(2,num):
        if num%i == 0:
            print "%d is not a prime number" %num
            return
    print "%d is a prime number" %num

for i in range(5):
    prime(i)