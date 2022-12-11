from pprint import pprint
list_ = [{'bin': bin(num), 'dec': num, 'oct': oct(num), 'hex': hex(num)} for num in range(16)]
pprint(list_)
