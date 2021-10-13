"""Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence
capitalized.
5.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT"""
lines = []
while True:
    s = input("Enter Lines :")
    if s:
        lines.append(s.upper())
    else:
        break
for sentence in lines:
    print(sentence)
# Leave input blank to stop