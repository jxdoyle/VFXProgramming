import os
os.system('cls' if os.name == 'nt' else 'clear')

file_name = "test.csv"

# Write File
try:
    print(f"Opening File {file_name} for append")
    test_file = open(file_name, "a") # append mode
except:
    print(f"There was an error opening {file_name}")
else:
    test_file.write(f"John, Doe, 42 {os.linesep}") # write line
    test_file.close() # close the file
finally:
    print(f"Finally {file_name}")

# Read File
try:
    print(f"Opening File {file_name} to read")
    test_file = open(file_name, "r") # read mode
except:
    print(f"There was an error opening {file_name}")
else:
    for line in test_file: # loop through file
        print(line)
    test_file.close() # close the file
finally:
    print(f"Finally {file_name}")