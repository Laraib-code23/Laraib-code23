#using condition
x=("abc",223,"apple","cherry","orange",9.56)
if "apple" in x:
    print("yes,'apple' is in given tuple:")
else:
    print("apple is not found:")
print(id(x))#show memory addresses