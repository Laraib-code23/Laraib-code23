#write a script takes a string from user and reversed that string then checked if the string is palindrome or not:
word=str(input("enter a string:"))
reversed_word=word[::-1]
if word==reversed_word:
 print("enter string is a palindrome!")
else:
 print("non palindrome:")
