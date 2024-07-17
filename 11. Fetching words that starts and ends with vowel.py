st = input("Enter Any String: ")

st = st.split()

lst =[]

for i in st:
    if i[0].lower() in 'aeiou' and i[-1].lower() in 'aeiou':
        lst.append(i)
print(lst)



#Output
'''
Enter Any String: Australia won more worldcups than India
['Australia', 'India']
'''
