st = "Tamilnadu cricket association council"

st_pascal = ''

for i in st.split():
    st_pascal = st_pascal + i[0].upper() + i[1:].lower()
print(st_pascal)
