st = "Python Narayana Tech House Hyderabad"


print([i for i in st.split() if len(i) == max([len(i) for i in st.split()])])

print([i for i in st.split() if len(i) == min([len(i) for i in st.split()])])







