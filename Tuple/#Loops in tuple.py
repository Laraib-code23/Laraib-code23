#Loops in tuple
#While loop
t=(23,34,54,12,35,89)
#i=0
#while i< len(t):
 #   print(t[i])
  #  i+=1
#Using For loop
reversed_tuple=()
for i in range(len(t) -1,-1,-2):
    reversed_tuple +=(t[i],)
    print(reversed_tuple)
    