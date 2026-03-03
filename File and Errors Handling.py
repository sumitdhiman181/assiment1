try:
    file = open("sample.txt",'r')
    print("Reading file content:")
    for index, line in enumerate(file):
        print(f"Line {index+1}: {line.strip()} ")
        #print(line.strip())  # Strip removes extra newline characters
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

