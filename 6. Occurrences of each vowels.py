st = input("Enter Any String : ")

vowels = 'aeiou'

dict_keys = {}.fromkeys(vowels,0)

for i in st:
    if i in dict_keys:
        dict_keys[i] = dict_keys[i] + 1
print(dict_keys)


