d=open("Q1.txt","r")
f2=open("delhi.txt","w")
f3=open("shimla.txt","w")
f4=open("others.txt","w")
da=d.read()
data=da.split("\n")
for i in range(0,len(data)):
    if "delhi" in data[i]:
        f2.write(data[i])
        f2.write("\n")
    elif "shimla" in data[i]:
        f3.write(data[i])
        f3.write("\n")
    else:
        f4.write(data[i])
        f4.write("\n")
f2.close()
f3.close()
f4.close()
d.close()
f2=open("delhi.txt","r")
f3=open("shimla.txt","r")
f4=open("others.txt","r")
print(f2.read())
print(f3.read())
print(f4.read())



# d=open("Q1.txt","r")
# f2=open("deilhi.txt","w")
# f3=open("shimla.txt","w")
# f4=open("others.txt","w")
# for i in d:
#     if "delhi" in i:
#         f2.write(i)
#     elif "shimla" in i:
#         f3.write(i)
#     else:
#         f4.write(i)
# f2.close()
# f3.close()
# f4.close()



