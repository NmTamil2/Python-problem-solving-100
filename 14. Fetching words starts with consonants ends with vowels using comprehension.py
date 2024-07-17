st =(input("Enter Any String: ")).split()

v= 'aeiouAEIOU'


result = [i for i in st if i[0] not in v and i[-1] in v]

print(result)
