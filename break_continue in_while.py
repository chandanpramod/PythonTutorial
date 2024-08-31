# break: Breaks out from the nearest enclosing loop
# continue: Go to the start of nearest enclosing loop
#
# #while <expression>:
#
#   <statement(s)>
#   break
#    <statement(s)>
#    continue
#    <statement(s)>
# <statement(s)>
# else clause:
#
# #while <expression>:
#   <statement(s)
# else:
#   <statement(s)

# x=0
# while x<=10:
#     print(x)
#     x+=1
#     break
#     print('In while loop')
# print('Out of while loop')

# x=0
# while x<=10:
#     print(x)
#     x+=1
#     continue
#     print('In while loop')
# print('Out of while loop')


# x=0
# y=0
# while x<=10:
#     print(x)
#     x+=1
#     print('1st while')
#     while y<=5:
#         print(y)
#         y+=1
#         break
#         print('inner while ')
#     print('Inner while ends')
# print('Loop ends')



# x=0
# while x<=10:
#     print(x)
#     x+=1
# else:
#     print('Loop is over')



# x=0
# while x<=10:
#     print(x)
#     x+=1
#     if x==5:
#         break
# print('Loop over')

x=0
while x<=10:
    print(x)
    x+=1
