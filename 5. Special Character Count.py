import string

st = 'na@ra#ya%na*'

count = 0

lowercase = string.ascii_lowercase     #string.ascii_uppercase(A-Z),string.ascii_letters(A-Z and a-z)

for i in st:
    if i in lowercase:
        continue
    else:
        count+=1
print(count)

