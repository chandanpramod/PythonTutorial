# PYTHON LIST METHODS
cities= ['Delhi','Mumbai','Melborn','Kolkata','Pune','Delhi','Mumbai','Melborn','Kolkata','Delhi','Mumbai','Melborn','Kolkata']
print(cities)
# list.append(x)
# cities.append('NaviMumbai')
# print(cities)
# • Add an item to the end of the list.
#
# list.insert(i, x)
# cities.insert(1,'Pune')
# print(cities)
# • Insert an item at a given position.
#
# list.remove(x)
# cities.remove('Delhi')
# print(cities)
# • Remove the first item from the list whose value is equal to x.
#
# list.pop([i])
# cities.pop(3)
# print(cities)
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
#
# list.index(x[, start[, end]])
# print(cities.index('Mumbai',0,4))
# print(cities.index('Melborn'))

# • Return zero-based index in the list of the first item whose value is equal to x.
#
# list.count(x)
# print(cities.count('Pune'))
# print(cities.count('Delhi'))
# • Return the number of times x appears in the list.
#
# list.sort(', key=None, reverse=False) • Sort the items of the list in place
# cities.sort()
# print(cities)

# list.reverse()
# cities.reverse()
# print(cities)
# • Reverse the elements of the list in place.
#
# list.copy()
# cities.copy()
# print(cities)
# • Return a shallow copy of the list. Equivalent to a[:].
#
# list.clear()
# cities.clear()
# print(cities)
# Remove all items from the list. Equivalent to del a[:].