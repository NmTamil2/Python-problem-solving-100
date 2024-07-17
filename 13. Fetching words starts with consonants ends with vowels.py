st = input("Enter Any String: ")

split_to_list = st.split()

v = 'aeiouAEIOU'

result = []

for i in split_to_list:
    if i[0] not in v and i[-1] in v:
        result.append(i)
print(result)
        
