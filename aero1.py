l1 = ["apple", "bomb", "cactus"]
out = {}

def count_char(string):
    ret_dict = {}
    for char in list(string):
        if ret_dict.get(char):
            ret_dict[char] = ret_dict[char] + 1
        else:
            ret_dict[char] = 1
    return ret_dict

for item in l1:
    temp_dict = count_char(item)
    min_val = min(temp_dict.values())
    min_key = [x for x,y in temp_dict.items() if y==min_val]
    out[item] = min_key[0]
print(out)
