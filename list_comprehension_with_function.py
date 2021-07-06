from copy import deepcopy
import collections

old_list = {"list": [{"name": "a", "age": 28},
                    {"name": "b", "age": 29},
                    {"name": "c", "age": 28}]}

new_list = {"list": [{"name": "aa", "age": 289}]}

def convert_list_to_dict(list1, list2):
    dict1 = dict(zip(tuple(range(len(list1))), tuple(sorted(list1))))
    dict2 = dict(zip(tuple(range(len(list2))), tuple(sorted(list2))))
    return dict1, dict2


def dict_merge(original_resource_dict, data_dict):
    resource_dict = deepcopy(original_resource_dict)
    for key, val in data_dict.items():
        if not resource_dict.get(key):
            resource_dict[key] = val
        elif isinstance(resource_dict[key], dict) and isinstance(data_dict[key], collections.Mapping):
            resource_dict[key] = dict_merge(resource_dict[key], data_dict[key])
        elif isinstance(resource_dict[key], list) and isinstance(data_dict[key], list):
            dict1, dict2 = convert_list_to_dict(old_list["list"], new_list["list"])
            resource_dict[key] = list(dict_merge(dict1, dict2).values())
#            resource_dict[key] = data_dict[key]
        else:
            resource_dict[key] = val
    return resource_dict

print(dict_merge(old_list, new_list))
#print(convert_list_to_dict(old_list["list"], new_list["list"]))