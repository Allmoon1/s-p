def connect_dicts(dict1, dict2):
    sum_values_dict1 = sum(val for val in dict1.values())
    sum_values_dict2 = sum(val for val in dict2.values())

    if  sum_values_dict1 >  sum_values_dict2 or ( sum_values_dict1 ==  sum_values_dict2 and len(dict1) < len(dict2)):
        priority_dict = dict1
        other_dict = dict2
    else:
        priority_dict = dict2
        other_dict = dict1

    merged_dict = {}

    for key, val in priority_dict.items():
        if val >= 10:
            merged_dict[key] = val

    for key, val in other_dict.items():
        if (key not in merged_dict) and (val >= 10):
            merged_dict.update({key:val})

    sorted_dict = dict(sorted(merged_dict.items(), key=lambda item: item[1]))

    return sorted_dict
    

print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 })) # =>{ "c": 11, "b": 12 }
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 })) # =>{ d: 11, "c": 12, "a": 13 }
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 })) # =>{ "c": 11, "b": 12, "a": 15 }