import collections

def dict_merge(rtn_dct, merge_dct):
    for k, v in merge_dct.items():
        if not rtn_dct.get(k):
            rtn_dct[k] = v
#        elif k in rtn_dct and type(v) != type(rtn_dct[k]):
#            raise TypeError(f"Overlapping keys exist with different types: original is {type(rtn_dct[k])}, new value is {type(v)}")
        elif isinstance(rtn_dct[k], dict) and isinstance(merge_dct[k], collections.Mapping):
            rtn_dct[k] = dict_merge(rtn_dct[k], merge_dct[k])
        elif isinstance(v, list):
            for list_value in v:
                if list_value not in rtn_dct[k]:
                    rtn_dct[k].append(list_value)
        else:
            rtn_dct[k] = v
    return rtn_dct