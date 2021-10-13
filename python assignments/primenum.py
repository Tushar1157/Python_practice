from functools import reduce
p= ([i for i in range(2, int(input("Enter your number: "))+1) if 0 not in [i%n for n in range(2, i)]])
print (p)
sum = reduce((lambda x, y: x + y), p)
print (sum)