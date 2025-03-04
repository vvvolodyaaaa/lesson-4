dct = {'person': {'in_dict': [1, 2, 3],
'after_list': {4, '5'},
'after_set': ('hello', )}}

dct_2 = {}
dct_2['person'] = 'person'
dct_2['in_dict'] = 'in_dict'
dct_2[1] = 1
dct_2[2] = 2
dct_2[3] = 3
num2 = [1, 2, 3,]
num3 = tuple(num2)
dct_2[num3] = [1, 2, 3,]
dct_2['after_list'] = 'after_list'
dct_2[4] = 4
dct_2['5'] = '5'
num = {4, '5'}
num_1 = tuple(num)
dct_2[num_1] = {4, '5'}
dct_2['after_set'] = 'after_set'
dct_2[('hello', )] = ('hello', )
print("test")
print(dct_2)