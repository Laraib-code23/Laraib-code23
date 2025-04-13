d={"Name":"Laraib","age":"23","degree":"Bcs",}
print(d)
#Update a exisiting key value
d.update({"degree":"Bechlor"}) 
print(d)
#to add new key
d.update({"f_color":"Black"})
print("Modified dictionary")
print(d)
print(d.keys())#print only keys
print(d.values())#print on;y values
d.pop("degree")#remove the specific key with value
print("Modified d")
print(d)
d1={"f_food":"Biryani","f_place":"Nelum","f_Color":"Black"}
#we can also use update method to add d1 into d and 
merged_dict={**d,**d1}
print(merged_dict)
