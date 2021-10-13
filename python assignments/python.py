#python
f= open("Delta_file.txt","w+")


f.write(input("Enter the string:- "))
f.close()
f= open("Delta_file.txt","r")
if f.mode =="r":
    contents = f.read()
    print (contents[::-1])


