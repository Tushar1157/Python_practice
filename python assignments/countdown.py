countDown =int (input("enter number to countdown :- 10"))
while (countDown >= 0):
    print(countDown)
    countDown = countDown - 1
    if countDown == 0:
        print("Action!")
        break