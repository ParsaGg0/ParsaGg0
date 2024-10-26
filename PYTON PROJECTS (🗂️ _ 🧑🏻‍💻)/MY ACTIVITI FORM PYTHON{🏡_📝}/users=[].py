users=[]
for i in range(1,11):
    x=input("enter your username")
    if x not in users:
        users.append(x)
        print(users)
    else:
        b =input(" 1 our suggested name or  2 your suggested name ?")
        if b==2:
            continue
        else:
         while x in users:
          reverse= x[::-1]
          x=x+reverse  
         users.append(x)
         print(x)
         print(users)        

        
