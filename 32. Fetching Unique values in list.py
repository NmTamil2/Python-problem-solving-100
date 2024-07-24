lst = [ "Tamil",10,20,30,10,"Tamil",1,True]


empty_list = []

for i in lst:
    if i not in empty_list:
        empty_list.append(i)

print(empty_list)
