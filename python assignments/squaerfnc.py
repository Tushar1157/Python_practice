n = int(input("Enter the number:-"))
def printValues():
	l = list() 
	for i in range(1,n+1):
		l.append(i**2)
	print(l)
		
printValues()
