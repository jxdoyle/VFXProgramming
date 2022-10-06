import os
os.system('cls' if os.name == 'nt' else 'clear')

# print float value as an integer
# similar to printf in c
# https://www.tutorialspoint.com/c_standard_library/c_function_printf.htm
students = 11.5
print("VFX Programmers : %2d" % (students))