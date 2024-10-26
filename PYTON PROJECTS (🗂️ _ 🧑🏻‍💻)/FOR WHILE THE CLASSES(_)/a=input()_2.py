a=input()
b=[]
m=0
for i in range(len(a)):
    if a[i]!=' ' :
        continue
    else:
        w=a[m:i]
        b.aapend(w)
        m=i+1
#
