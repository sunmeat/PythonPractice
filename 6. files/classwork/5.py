file1 = open("file1.txt","w")

string = []
string.append("Hello\n")
string.append("world\n")
string.append("qqqqqqq\n")
string.append("wwwwwwww\n")

for a in string:
    file1.write(a)
file1.close()

file2=open("rez.txt","w")

# with open("file1.txt","r") as f:
#     text = f.readlines()
#     for a in text:
#         file2.write(a)   
# with open("file1.txt","r") as f:
#     text = f.readlines()
#     text.reverse()
#     for a in text:
#        file2.write(a)

  

file2.close()




