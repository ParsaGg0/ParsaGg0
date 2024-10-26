mahdi=[]
mani=[]
scr_mani=0
scr_mahdi=0
for i in range(1,6):
 x=int(input())
 mani.append(x)
for i in range(1,6):
  x=int(input())
  mahdi.append(x)
for i in range(0,5):
  if mani[i]>mahdi[i]:
   scr_mani= scr_mani+1 
  else:
     scr_mahdi= scr_mahdi+1 
if scr_mahdi>=3:
  print("mahdi")
if scr_mani>=3:
  print("mani")