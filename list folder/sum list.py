a=[2,3,6,8,4]
reversed_numbers=a[::-1]# here it reversed the whole list it is a slicing 
print("The reverse of the list is:",reversed_numbers)
total=sum(a)
print(total)

#Here we also go with user input 

numbers=[]
for i in range(5):
    num=int(input(f"enter number{i+1}:"))
    numbers.append(num)# Here append use to modify the list
total=sum(numbers)
print("This is the sun of your provided numbers:",total)
# Removing duplicates in aprogram without using sets()
numbers =[2,4,5,6,6,2,0,9,9,1,2,1,1,3,4,5,6,78]
unique_numbers=[]
for num in  numbers:
 if num not in unique_numbers:
   unique_numbers.append(num)
print("List after removving duplicates:",unique_numbers)