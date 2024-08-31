# Write file

with open("C:\\Users\\Admin\\Desktop\\File Handling\\testfile4.txt","w") as fw:
    fw.write("Hi My name is Pramod")


# Read file
with open("C:\\Users\\Admin\\Desktop\\File Handling\\testfile4.txt",'r') as fr:
    print(fr.read())


# Append

with open("C:\\Users\\Admin\\Desktop\\File Handling\\testfile4.txt",'a') as fap:
    fap.write("I am 35 years old")
