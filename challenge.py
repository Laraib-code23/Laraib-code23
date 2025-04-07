name = str(input("Enter your full name: "))
print(name.upper())
print(name.lower())
print("Number of letters (excluding spaces):", len(name.replace(" ", "")))
full_name = name.split()
first_name = full_name[0]
last_name = full_name[1]
print("First name:", first_name)
print("Last name:", last_name)