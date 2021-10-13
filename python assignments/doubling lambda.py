L =list(filter(lambda x: x%5==0, range(1,1000)))
print("The list of numbers divisible by 5 in  Range of 1 tyo 1000 : \n",L)
def double(integer):
    return integer*2

doubling = list(map(double,L))
print("\nList of all elements of L doubled : \n", doubling)
