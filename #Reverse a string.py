#Reverse a string
def reverse(s):
    return s[::-1]
text=input("Enter a string:")
reversed_text = reverse(text)
print(f"The reversed string is:{reversed_text}")    