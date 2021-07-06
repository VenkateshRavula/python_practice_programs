
def my_gen(n):
    for i in range(n):
        yield i*i

a = my_gen(3)
print(next(a))
print(next(a))
print(next(a))
print(next(a))

