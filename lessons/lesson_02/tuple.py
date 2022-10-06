import os
os.system('cls' if os.name == 'nt' else 'clear')

sample_tuple = ('one','two','three',1, 2, 3)
print(sample_tuple)
print(hex(id(sample_tuple)))

sample_tuple += ('four','five','6',4, 5, 6)

print(sample_tuple)
print(hex(id(sample_tuple)))

sample_tuple = sample_tuple + sample_tuple

print(sample_tuple)
print(hex(id(sample_tuple)))

sample_tuple = sample_tuple * 2

print(sample_tuple)
print(hex(id(sample_tuple)))

tuple_as_a_list = list(sample_tuple)
list_as_tuple = tuple(tuple_as_a_list)