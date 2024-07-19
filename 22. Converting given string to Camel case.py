st= "Indian cricket council association"

lst = st.split()

camel = ''

for i in lst[1:]:
    camel = camel + i[0].upper() + i[1:].lower()
camel = lst[0].lower() + camel
print(camel)
