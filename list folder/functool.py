#find max using reduce:
'''
Functool is a built in python module that provides higher order functions--- these are functions that act on or return other functions

'''
from functools import reduce
numbers=[3,7,1,9,2]
maximum=reduce(lambda a,b: a if a>b else b, numbers)
print("The maximum numbers is:",maximum)
#here we also use user define numbers:
numbers=list(map(int,input("Entern 5 numbers seperated by space:").split()))
if len(numbers)!=5:
     print("Please enter exactly 5 values:")
else:     
     maximum=reduce(lambda a,b: a if a>b else b, numbers)
     print("The maximum numbers is:",maximum)