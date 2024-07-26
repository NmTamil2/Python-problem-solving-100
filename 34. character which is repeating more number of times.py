st = "narayana"

unique = set(st)

dictionary = {}.fromkeys(unique,0)

for i in st:
    dictionary[i] = dictionary[i]+1

for j in dictionary:
    
    if dictionary[j] == max(dictionary.values()):
        print('{} is repeated {} times in string' .format(j,dictionary[j]))
     






    
    
    
