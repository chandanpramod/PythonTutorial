# Tuples are idexed, allow duplicated but immtable/can not modified or changed
tup1= (1,2,3,4,1,2,3,4,1,2,3,4)
tup2=('A','B','C','A')
tup3=(True,False)
tup4=(True, 10, 'C', 10.30, True)
# print(tup1[0])
# print(tup4)
# print(len(tup2))
# print(type(tup3))
#Count():
# print(tup4.count(True))
# print(tup1.count(1))
# print(tup1.count(6))
# # index:
# print(tup1.index(4))
#Len()
# print(len(tup1))
#type()
# print(type(tup1))
# print(tup1[6])
# for i in tup1:
#     print(i)

addTup=tup1+tup2
print(addTup)
print(addTup[0:4])