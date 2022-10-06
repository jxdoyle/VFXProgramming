import os
os.system('cls' if os.name == 'nt' else 'clear')

sample_dictionary = {'player1':"FIFA Expert"}

result = sample_dictionary['player1']
print(result)
print(hex(id(sample_dictionary)))