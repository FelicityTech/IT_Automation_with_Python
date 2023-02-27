f = open("sample.txt", "r")
# move to 11 character
f.seek(11)
# read from 11th character
print(f.read())
