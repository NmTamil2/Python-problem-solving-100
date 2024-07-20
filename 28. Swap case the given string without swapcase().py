st = "CricKet"

result = ''

for i in st:
    if i.isupper():
        result = result + i.lower()
    else:
        result = result + i.upper()
print(result)
        
