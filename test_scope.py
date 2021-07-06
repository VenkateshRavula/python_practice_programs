a = {'name': 'scope-1',
     'addResourceUris': ['apple', 'ball', 'dog']}

b = {'name': 'scope-2',
     'addResourceUris': ['apple', 'ball', 'dog1'],
	 'removedResourceUris': ['balls']}

c = {'name': 'scope-3',
     'addResourceUris': ['apple', 'eagle'],
	 'removedResourceUris': ['ball1', 'bat']}

d = {'name': 'scope-4',
     'addResourceUris': ['ball', 'dog']}

e = {'name': 'scope-5',
     'removedResourceUris': ['apple', 'ball', 'dog']}


def compare_resource_assignments(current_dict, updated_dict):
    changed = False
    if updated_dict.get('removedResourceUris'):
        common_elements = set(current_dict['addResourceUris']).intersection(set(updated_dict['removedResourceUris']))
        if len(common_elements) > 0:
            changed = True
        else:
            updated_dict.pop('removedResourceUris')
    if changed is True:
        return changed, updated_dict

    if current_dict.get('addResourceUris') and updated_dict.get('addResourceUris'):
        all_add_elements = set(current_dict['addResourceUris']).union(set(updated_dict['addResourceUris']))
        new_elements = all_add_elements - set(current_dict['addResourceUris'])
        if len(new_elements) > 0:
            changed = True

    return changed, updated_dict


change, result = compare_resource_assignments(a, b)
print(change)
print(result)