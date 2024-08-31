s1={10,20,30}
s2={10,20,30,'Ram','Laxman'}
s3={'20','30'}
s4=set((10,20,30,40,50,60,70,80))
L1=[10,20,30,40,50,60,70,80,90,100]
s5=set(L1)
# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(L1)
# print(s5)
# print(len(s1))
# print(10 in s1)
# print(900 in s1)



# add(ele): Add element in to the set
# s1.add('Pramod')
# print(s1)
# s1.add(10)
# print(s1)
# remove(ele): removee the element from the set if not present show the keyerror.
# s1.remove(10)
# print(s1)
# s1.remove('Pramod')
# print(s1)


# discard(elem)-Remove element elem from the set if it is present. pop)-Remove
# s1.discard(10)
# print(s1)
# s1.discard('Pramod')
# print(s1)
# pop() - remover and return an arbitrary element from the set. Raises KeyError if the set is empty.
# s1.pop()
# print(s1)
# clear()-Remove all elements from the set
# s1.clear()
# print(s1)
# Joining two sets
#
# union()
# newSet=s1.union(s2)
# print(newSet)

# update
# s1.update(s2)
# print(s1)
# Keep only duplicates

# intersection()
# newSet=s1.intersection(s2)
# print(newSet)

# intersection_update()
# s1.intersection_update(s2)
# print(s1)


# Keep all excluding duplicates

# symmetric difference()
# newSet=s1.symmetric_difference(s2)
# print(newSet)
# symmetric_difference_update()
# s1.symmetric_difference_update(s2)
# print(s1)


# Returns set containing difference between two or mo difference
# difference()
# newSet=s1.difference(s2)
# newSet1=s2.difference(s1)
# print(newSet)
# print(newSet1)
# difference_update()
# s1.difference_update(s2)
# print(s1)
# issubset()
# print(s1.issubset(s2))
# print(s2.issubset(s1))
# issuperset
print(s1.issuperset(s2))
print(s2.issuperset(s1))