import os
os.system('cls' if os.name == 'nt' else 'clear')

sample_string = "This is the 'one','two','three',1, 2, 3"
print(sample_string)
print(hex(id(sample_string)))

sample_string += "'four','five','6',4, 5, 6"

print(sample_string)
print(hex(id(sample_string)))

# Take a slice of the string
string_first_slice = sample_string[1:6]
print(string_first_slice)
print(hex(id(string_first_slice)))

# Take a slice with a negative index
string_second_slice = sample_string[1:-1]
print(string_second_slice)
print(hex(id(string_second_slice)))

# Take a slice which goes right to the end 'omit' second index
string_third_slice = sample_string[1:]
print(string_third_slice)
print(hex(id(string_third_slice)))

# Take a full copy '[:]'
string_fourth_slice = sample_string[:]
print(string_fourth_slice)
print(hex(id(string_fourth_slice)))

# Test if a value is in a container "String"
print('1' in sample_string)
print('Once' in sample_string)

test = sample_string[2:7]
print(test)
print('is' in test)