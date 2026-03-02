fh = open("simple.txt","xt")
fh.write("reading file content.\nline1: this is a simple txt file.\nline2: it contains multiple lines")

fh.close()

fh = open("simple.txt","rt")
lines = fh.readlines()

fh.close()
for line in lines:
    print(line.rstrip('\n'))
