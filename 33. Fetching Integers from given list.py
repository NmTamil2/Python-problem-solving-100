lst =[True,15,"Tommy",False,23,"Jack",34.5,None]


lst1 =[]

for i in lst:
    if type(i) == int :
        lst1.append(i)

print(lst1)
