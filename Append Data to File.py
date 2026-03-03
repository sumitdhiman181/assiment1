file1 = open("output.txt", 'w')
file_input = input("Enter text to write to the file: ")
writing_file = file1.write(file_input)
print("Data successfully written to output.txt")
file1.close()

file1 = open("output.txt", 'a')
append_input = input("Enter additional text to append: ")
append_file = file1.write("\n" + append_input)
print("Data successfully appended.")
file1.close()

file1 = open("output.txt", 'r')
read_file = file1.read()
print("Final content of output.txt.\n",read_file)
file1.close()


