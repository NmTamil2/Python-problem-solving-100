st = input("Enter Any String: ")

v = 'aeiouAEIOU'

result = [ i for i in st if i not in v]

print(result)
