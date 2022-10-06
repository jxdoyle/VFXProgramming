import os
os.system('cls' if os.name == 'nt' else 'clear')

sample_string = ('one','two','three',1, 2, 3)
print(sample_string)
print(hex(id(sample_string)))

sample_string += ('four','five','6',4, 5, 6)

print(sample_string)
print(hex(id(sample_string)))

print(sample_string * 2)

sample_string = sample_string + sample_string
print(sample_string)
print(hex(id(sample_string)))