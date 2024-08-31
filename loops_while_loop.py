# Used to iterate block of code as long as test expression is true Test expression is checked first,
# if expression is evaluated to true then body of loop is executed Conditions are used to stop the loops
#
# Can iterate on list, strings, tuples, dictionary
#
# while test_expression:
# body of while loop
# x=0
# while x<=10:
#     print(x)
#     x+=2
# print('out of loop')

# city='Ahmednagar'
# x=0
# while x<len(city):
#     print(city[x])
#     x+=1


digit=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x=0
print('All Numbers as below')
while x<=len(digit):

    print(x)
    x+=1

digit=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x=0
print('Even Numbers as below')
while x<=len(digit):

    print(x)
    x+=2

digit=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x=1
print('Odd Numbers as below')
while x<=len(digit):

    print(x)
    x+=2