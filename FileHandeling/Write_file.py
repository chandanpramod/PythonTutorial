# Manual steps:
# Open and create filecm
# write in to the file
# save and close
#
#
#   Mode:
#   Write: w
#   read: r
#   append: a
#   read/write:r+
# We need to use builin function

# F1= open("C:\\Users\\Admin\\Desktop\\File Handling\\testfile.txt","w")
# F1.write("I am Pramod")
# F1.close()

f=open("C:\\Users\\Admin\\Desktop\\File Handling\\testfile2.txt","w")
l=[1,2,3,4,5,6,7,8,9,0]
for i in l:
    f.write(str(i)+"\n")
f.close()


f1=open("C:\\Users\\Admin\\Desktop\\File Handling\\testfile3.txt","w")
dict={"A": "Aus","B":"Ban"}
for i in dict.items():
    f1.write(str(i)+"\n")
f1.close()