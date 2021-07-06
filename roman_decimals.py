inp = input("Enter your input: ")
roman_dict = {1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}

keys_list = sorted(dict.keys(roman_dict))
list1 = []

def roman(inp):
    for i in reversed(keys_list):
        if inp >= i and inp != 0:
            inp -= i
            list1.append(roman_dict[i])
            roman(inp)
            return

roman(inp)
print ''.join(list1)