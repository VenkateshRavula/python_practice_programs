# def test_list(a, l=[]):
#     l.append(a)
#     return l
#
# list1 = test_list(10)
# list2 = test_list(123, [])
# list3 = test_list('a')
#
# print(list1) #[10]
# print(list2) #[123]
# print(list3) #['a']

# ================================
list1 = [[]] * 5
print(list1)
list1[0].append(10)
print(list1)
list1[1].append(20)
print(list1)
list1.append(30)
print(list1)

# s1 = "123.45"
# ret = eval(s1)
# print("{} - {}".format(ret, type(ret)))

s1 = "venkatesh"
for i in s1:
    if s1.count(i) == 1:
        print(i)