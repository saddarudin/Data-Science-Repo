# Write a program to merge two dictionaries. If there are common keys, sum their values.
# If a key is unique to one dictionary, include it in the merged dictionary.

def merge_dict(dict_a, dict_b):
    dict_c = dict_a
    for key in dict_b:
        if key not in dict_c:
            dict_c[key] = dict_b[key]
        else:
            dict_c[key] = dict_a[key]+dict_b[key]
    return dict_c


dict_one = {
    "a": 1,
    "b": 2,
    "c": 3
}

dict_two = {
    "d": 1,
    "e": 5,
    "b": 3
}

merged_dict = merge_dict(dict_one, dict_two)
print(merged_dict)
