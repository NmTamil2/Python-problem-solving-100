st= 'Na@ra% ya#na &7634 '

import string


result = [ i for i in st if i not in string.ascii_letters and i != ' ' and i not in string.digits ] 

print(result)
