''' LIST FUNCTION  FOR INSERTIN ELEMENTS-----
1= insert{list_name.insert(index,inserting_element)} :- insert will insert the element given index

2= append{list_name.append(inserting_element)}:-  append will insert the element at last position

3= extend{list_name.extend(inserting_object)}:-  extend will insert the all element of the object
                                                 at the last '''


l=[12,43,53,22,11]
print(l)
l.insert(0, 1)  
print(l)

print()
l1=[55,33,44,22,11]
print(l1)
l1.append(1)
print(l1)

print()
l2=[11,22,33,44,55]
print(l2)
l2.extend(l1)
print(l2)