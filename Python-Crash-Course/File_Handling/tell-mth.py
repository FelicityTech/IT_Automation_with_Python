f = open("sample.txt", "r")
# read first line
f.readline()
# get current position of file handle
print(f.tell())

# The tell() method to return the current position of 
# the file pointer from the beginning of the file