lst = [4, '5', '6', 8]
# используя join получить '4568'

new_list = [str(x) for x in lst]
string = ''.join(new_list)
print(string)
