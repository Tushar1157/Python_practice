number=int (input("Enter the number to create dict.:- "))
numberDict = {}
for i in range(1, number+1):
    numberDict[i] = i*i

print(numberDict)
