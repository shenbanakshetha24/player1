nu1,nu2=map(int,input().split())
k=[]
for i in range(nu1+1,nu2+1):
 if i>1:
  for r in range(2,i):
   if(i%v==0):
    break
   else:
    k.append(r)
    print(len(k)+1)
