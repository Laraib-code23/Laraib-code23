#here we define tuple
#Tuple is a collection of ordered and immutable elements.Once tuple created ,it cannot modify 
my_tuple=(1,2,3,4,5)
print(my_tuple)
#try to modify 
#my_tuple[0,1,2,3,4]=(2,3,7,1,5)
#print(my_tuple)
#It allows duplicates also
t=("apple","banana","apple","apple","cherry")
print(t)
print(len(t)) #tell about length
#Remainder to create s single item ,u have to add a comma after item,otherwise python does not recognize it
#s=("apple") here it takes it as a string not a tuple
#print(s)
s=("apple",)
print(s)
tuple1=("String",123,0.34,True,"sum")
print(tuple1)
