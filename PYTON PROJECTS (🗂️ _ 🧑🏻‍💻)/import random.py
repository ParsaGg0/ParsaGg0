import random
a=[0,1]
scr_cmp=0
scr_user=0
x=random.choice(a)
y = input("enter your number")
print('computer guess:',x)
if x==y:
    scr_cmp = scr_cmp+1
else:
    scr_user = scr_user+1
print('user:',scr_user)
print ('cmp:',scr_cmp)