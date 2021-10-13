#2.Write a python script to take input from user (String) and to verify it whether string is Symmetrical or Palindrome.

def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = input("Enter the string: ")
ans = isPalindrome(s)
 
if ans:
    print("The given string is pallindrome!")
else:
    print("The given string is not pallindrome!")