l1 = []
l2 = []
#number of elements in the list 
while(True):
  n = int(input("enter number of elements for list1:"))
  m = int(input("enter number of elements for list2:"))
  if(n!=m):
    print("enter same lengths for the lists")
  else:
    break
print("enter elements into list1:")
for i in range(0,n):
 ele = int(input())
  l1.append(ele)
  
print("enter elements into list2:")
for i in range (0,m):
  ele = int(input())
  l2.append(ele)
print("list1 is ",l1,"list2 is ",l2)
def mult_lists(a,b):
  product=[i*j for i,j in zip(a,b)]
  print(product)
  return sum(product)
print("The sum of the products of corresponding elements is :",mult_lists(l1,l2))
