text = "This is new content"
# writing new content to the file
fp = open("write_demo.txt", "w")
fp.write(text)
print('Done Writing')
fp.close()