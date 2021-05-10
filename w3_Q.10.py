file=open("Q1.txt","r")
a=file.read().split()
i=0
empty=[]
while i<len(a):
    c=0
    e=[]
    j=0
    while j<len(a):
        if a[i]==a[j]:
            c+=1
        j+=1
        e.append(a[i])
        e.append(c)
        if e not in empty:
            empty.append(e)
        i=i+1
    print(empty)
    file.close()



    