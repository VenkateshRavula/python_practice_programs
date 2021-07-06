inp_num = str(input("enter input number: "))

def next_max(num):
    rev_num = num[::-1]
    list_num = list(num)
    for i in range(len(list_num)-1):
        if list_num[-i-1] > list_num[-i-2]:
            list_num[-i-1], list_num[-i-2] = list_num[-i-2], list_num[-i-1]
        new_num = int(''.join(list_num))
        out1 = int(''.join(list_num[:-i] + sorted(list_num[-i:])))
        if new_num > int(num):
            if int(num) < out1 < new_num:
                return out1
            return new_num
    return int(''.join(list_num))

print(next_max(inp_num))
