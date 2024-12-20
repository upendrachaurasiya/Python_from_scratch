'''    List function -----
1- del {del list_name(index_num)} :-   delete elements of the list from given index number

2- pop {list_name.pop(index_num)}  :-   pop also delete ements from the list but return delete elements also

3- remove{list_name.remove(value_from_list)}  :- remove delete the element from the list from given element

4- clear(list_name.clear())      :- clear will blank the list'''



l1=[3,5,2,5,53]
print(l1)
del l1[2]
print(l1)
print()


l2=[1,2,3,4,5,6]
print(l2)
print(l2.pop(0))
print(l2)
print()



l3=[5,3,33,552.2,666]
print(l3)
l3.remove(552.2)
print(l3)