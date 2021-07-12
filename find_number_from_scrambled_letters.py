
# Scenario: Your friend wants to share a contact number which is confidential. To ensure
# confidentiality he converted the numeric number to String. Ex: 9 -> NINE and then Randomized the
# string which can be anything like ENIN. And dropped that info before your room in a piece of paper

#write in your logic to decode that 

# EX1:  ETHER --> THREE -> 3
# EX2: OZONETOWER --> ZERO ONE TWO -> 012
from collections import OrderedDict
inp = "OZONETOWERROUFVEIF"

dict_of_numbers = {
    "ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5,
    "SIX": 6, "SEVEN": 7, "EIGHT": 8, "NINE": 9, "ZERO": 0
}

primary_letters = {
    'W': 'TWO', 'U': 'FOUR', 'X': 'SIX', 'G': 'EIGHT', 'Z': 'ZERO'
}

secondary_letters = OrderedDict()
secondary_letters['O'] = 'ONE'
secondary_letters['H'] = 'THREE'
secondary_letters['F'] = 'FIVE'
secondary_letters['S'] = 'SEVEN'
secondary_letters['N'] = 'NINE'

def remove_substring(main_list, sub_string):
    # this will remove the substring from main list and
    # returns the remaining string
    try:
        for char in list(sub_string):
            main_list.remove(char)
    except ValueError as e:
        print("{} - {}".format(main_list, sub_string))
        raise Exception(e)
    return "".join(main_list)

out_list = []
copy_inp = inp

for p_key in primary_letters.keys():
    sorted_inp = sorted(copy_inp)
    if p_key in sorted_inp:
        count = sorted_inp.count(p_key)
        print("{} repeated {} times - {}".format(p_key, count, sorted_inp))
        for _ in range(count):
            copy_inp = remove_substring(sorted_inp, primary_letters[p_key])
            out_list.append(primary_letters[p_key])

while len(copy_inp) != 0:
    for s_key in secondary_letters.keys():
        sorted_inp = sorted(copy_inp)
        print("secondary loop - {} - {}".format(s_key, sorted_inp))
        if s_key in sorted_inp:
            copy_inp = remove_substring(sorted_inp, secondary_letters[s_key])
            out_list.append(secondary_letters[s_key])
            if len(copy_inp) == 0:
                break

final_list = sorted([dict_of_numbers[i] for i in out_list])
print(final_list)
