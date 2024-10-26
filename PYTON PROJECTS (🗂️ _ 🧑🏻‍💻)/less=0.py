less=0
equal=0
more=0
for i in range(1,21):
    x=int(input())
    if x>3:
        more=more+1
    elif x==3:
     equal=equal+1
    elif x<3:
     less=less+1
print(less)
print(equal)
print(more)