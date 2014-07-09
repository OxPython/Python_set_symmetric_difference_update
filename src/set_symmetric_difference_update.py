'''
Created on Jul 9, 2014

@author: viejomer

How to remove the same elements of two or more sets while retaining 
those who are different?

¿Cómo eliminar a los mismos elementos de dos o más conjuntos, 
conservando los que son diferentes?

symmetric_difference_update(other)
set ^= other
Update the set, keeping only elements found in either set, but not in both.
'''

#Result set
r = set()

#Create a set with values.
s_1 = set([0,1,2,3])
print("set one", s_1)

s_2 = set([1,6])
print("set two", s_2)

#Using symmetric_difference_update
#This example keep all the values from s_1
r.symmetric_difference_update(s_1)
print("This set have the items from both sets",r) 

#Usingsymmetric_difference_update
#This example keep all the values that are not equals in both sets
r.symmetric_difference_update(s_2)
print("This set have the items from both sets",r) 