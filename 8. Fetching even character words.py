st = input("Enter Any String: ")

split_to_List = st.split(" ")

even_characters = []

for i in split_to_List:
    if len(i) % 2 == 0:
        even_characters.append(i)
print(even_characters)
        
