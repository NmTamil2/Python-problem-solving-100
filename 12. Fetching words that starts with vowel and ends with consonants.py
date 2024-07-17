st = input("Enter Any String: ")

split_to_list = st.split()

result = []

for i in split_to_list:
    if i[0].lower() in 'aeiou' and i[-1].lower() not in 'aeiou':
        result.append(i)
print(result)
