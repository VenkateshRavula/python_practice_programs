inp_list = input("Enter the input list: ")
if len(inp_list) == 0:
    raise Exception("Input list should not be empty")

rounds = inp_list[0]
final_index = inp_list[-1] - 1
final_list = range(1,101)

def recursive_func(list1, piles):
    out_list = []
    for pile in range(piles):
        pile_list = list1[pile::piles]
        out_list.extend(pile_list)
    return out_list

for round in range(1, rounds+1):
    print(">>>>>>>> Round - {}".format(round))
    final_list = recursive_func(final_list, inp_list[round])
    print final_list

print final_list[final_index]