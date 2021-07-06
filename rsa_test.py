# for i in range(1,101):
#     res = ""
#     if i % 3 == 0:
#         res = "fizz"
#     if i % 5 == 0:
#         res += "buzz"
#     if len(res) == 0:
#         print(i)
#     else:
#         print(res)

# dict1 = {'1':1, '2':2, '3':3, '4':4, '5':5,
#          '6':6, '7':7, '8':8, '9':9, '0':0}
# inp1 = "12345"
# len_str = len(inp1)
# output = 0
# for i in inp1:
#     ret = dict1[i] * (10**(len_str-1))
#     len_str -= 1
#     output += ret
#
# print("{} - {}".format(output, type(output)))

str1 = "venkatesh"
d = {}
for i in str1:
    if d.get(i):
        d[i] = d[i] + 1
    else:
        d[i] = 1

for k,v in d.items():
    if v == 1:
        print(k)

def my_dec(func):
    def inner(a,b):
        print("before func")
        func(a,b)
        print("after func")
    return inner

@my_dec
def sum_of_integers(a,b):
    return a+b
