def isBalanced(s):
    # Write your code here
    temp_dict = {
        '}': '{', ')': '(', ']': '['
    }
    temp_list = []

    # if i is in open paranthesis list, then add it to temp_list
    # if i is in closed paranthesis list, then check if last item
    # in temp_list is matching pair of i. If so, then pop that item
    # By end all of iterations, temp_list should be empty
    for i in s:
        if i in temp_dict.values():
            temp_list.append(i)
        elif i in temp_dict.keys():
            if not temp_list or temp_list.pop() != temp_dict[i]:
                return "NO"

    if temp_list:
        return "NO"
    else:
        return "YES"


inp = "{(([])[])[]}"
print(isBalanced(inp))