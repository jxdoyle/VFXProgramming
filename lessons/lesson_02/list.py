import os
os.system('cls' if os.name == 'nt' else 'clear')

sample_list = ['one','two','three',1, 2, 3]
print(sample_list)
print(hex(id(sample_list)))

sample_list.append('four')

print(sample_list)
print(hex(id(sample_list)))

sample_list.append(['five','6',4, 5, 6])

print(sample_list)
print(hex(id(sample_list)))

sample_list.insert(3, 'four')

print(sample_list)
print(hex(id(sample_list)))

sample_list.extend(['Seven','8',9, 10, 11])

print(sample_list)
print(hex(id(sample_list)))

sample_list.reverse()
print(sample_list)
print(hex(id(sample_list)))


idx = sample_list.index('one')
del sample_list[idx]

count = sample_list.count('two')
print(count)

sample_list.remove('three')
sample_list.remove('four')

del sample_list[7]

print(sample_list)
print(hex(id(sample_list)))

sample_list = [1, 2, 5, 4]
sample_list.sort()
print(sample_list)
print(hex(id(sample_list)))
