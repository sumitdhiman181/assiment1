
fh = open("output.txt","wt")
fh.write("Enter the text to the file: Hello, Python.\n")
fh.write("Data successfull write to output.txt.")
fh.close()
print()


fh = open("output.txt","at")
fh.write("\nEnter to additional to append : learning file handling in python.\n")
fh.write("Data successfully append.")


fh.write("\nEnter the text to the file: Hello, Python.\n")
fh.write("Hello,python!\n")
fh.write("learning file handling in python.")
fh.close()

fh = open("output.txt","rt")
content = fh.read()
fh.close()
print(content)
