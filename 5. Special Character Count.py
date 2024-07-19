import string

st = 'na@ra#ya%na*'

count = 0

letters = string.ascii_letters     #string.ascii_uppercase(A-Z),string.ascii_letters(A-Z and a-z)

for i in st:
    if i in letters:
        continue
    else:
        count+=1
print(count)

