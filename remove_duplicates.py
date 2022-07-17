from collections import OrderedDict
string =input("please enter a string ")
#with order of the string maintained 
def remove_duplicates1(string):
  new_string="".join(OrderedDict.fromkeys(string))
  if new_string:
    return (new_string,len(string)-len(new_string))
  else:
    print("please provide only alphabets")
    
s = remove_duplicates1(string)
print(string,"after duplicates removed ordered is:",s)
#without order of the string maintained
def remove_duplicates2(string):
  new_string = "".join(set(string))
  if new_string:
    return(new_string,len(string)-len(new_string))
  else:
    print("please provide only alphabets")

s = remove_duplicates2(string)
print(string,"after duplicates removed unordered is :",s)
