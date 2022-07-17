from array import  *
a=array('i',[2,3,4,5])
n=int(input("enter search element : "))
for i in a:
	 if(i==n):
	 	  print("found")
	 	  print(a.index(i))
	 	  break
else:
	     print("not found")
