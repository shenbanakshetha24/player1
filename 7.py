fg=input()
fg=list(fg)
res=""
for i in range(0,len(fg)-1,2):
 temp=fg[i+1]
 fg[i+1]=fg[i]
 fg[i]=temp
print(res.join(fg))
