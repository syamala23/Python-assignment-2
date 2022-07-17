a="syamala"
cntc=0
cntl=0
cnt=0
for i in a:
  if(i.isupper()):
    cntc+=1
  elif(i.islower()):
    cntl+=1
  else:
    cnt+=1

print("no of digits : ",cnt)
print("no of lowercase letters : ",cntl)
print("no of upper case letters : ",cntc)
