a = open("myfile", "a")
a.write("this is python")
a.close()
a = open("myfile.txt", "r")
print(a.read())


