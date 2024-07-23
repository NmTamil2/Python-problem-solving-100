dictionary = { 'a':10, 'b':20, 'c':30 }

convert_to_dict_items = dictionary.items()

convert_to_list = list(convert_to_dict_items)

convert_to_list.reverse()

repeat_to_dict = dict(convert_to_list)

print(repeat_to_dict)


