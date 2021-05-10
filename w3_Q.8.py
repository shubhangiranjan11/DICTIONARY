file=open("Q3.txt","r")
a=file.readlines()
i=0
max=(a[0])
while i<len(a):
    j=0
    while j<len(a):
        if len(a[i])>len(a[j]):
            if len(a[i])>len(max):
                max=(a[i])
        j+=1
    i=+1
print(max)
file.close








