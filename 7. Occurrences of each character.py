st = input("Enter Any String: " )

set_conv = set(st)

d = {}.fromkeys(set_conv, 0)

for i in st:
    d[i] = d[i]+1
print(d)
