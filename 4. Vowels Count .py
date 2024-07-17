##st = input("Enter Any String: ")
##
##count = 0
##
##v = 'aeiouAEIOU'
##
##for i in st:
##    if i in v:
##        count = count + 1
##print(count)


st = input("Enter Any String: ")

count = 0

v = 'aeiou'

for i in st:
    if i.lower() in v:
        count = count + 1
print(count)

