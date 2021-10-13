import string
import random
  
# initializing size of string 
N = int(input("enter lent of string:- "))
  
# using random.choices()
# generating random strings 
res = ''.join(random.choices(string.ascii_lowercase, k = N))
  
# print result
print("The generated random string : " + str(res))