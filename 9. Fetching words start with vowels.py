st = input("Enter Any String: ")

split_to_list = st.split()


for i in split_to_list:
    if i[0].lower() in 'aeiou':
        print(i)
