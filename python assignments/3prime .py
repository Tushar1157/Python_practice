#Write a python script to Print prime numbers below 100.

lower =0
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 0:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)