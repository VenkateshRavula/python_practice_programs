def minimum_swaps(arr):
    ref_arr = sorted(arr)
    index_inp_dict = {v:i for i,v in enumerate(arr)}
    swaps = 0

    for i,v in enumerate(arr):
        expected_val = ref_arr[i]
        if expected_val != v:
            target_index = index_inp_dict[expected_val]
            arr[i], arr[target_index] = arr[target_index], arr[i]
            index_inp_dict[v] = target_index
            index_inp_dict[expected_val] = i
            swaps += 1
    return swaps

arr = [2,3,4,1,5]
print(minimum_swaps(arr))