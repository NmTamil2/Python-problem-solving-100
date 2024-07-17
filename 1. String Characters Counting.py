st = input('Enter Any String: ')

count = 0

for i in st:
    if i == ' ':
        continue
    else:
        count = count+1
print(count)
    