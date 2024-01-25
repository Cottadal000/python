file = open("AFile.txt","w")
file.write("Here's some stuff\n")
file.close()

twofile = open("AFile.txt", "r")
print(twofile.read())
twofile.close()