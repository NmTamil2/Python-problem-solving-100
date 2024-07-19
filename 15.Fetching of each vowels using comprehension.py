st = input("Enter Any String: ")

v = 'aeiouAEIOU'

result = [ i for i in st if i in v]

print(result)
