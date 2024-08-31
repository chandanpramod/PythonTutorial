# Positional Argument
# Keyword argument
# Required Argument
# Optional Argument

#Positional Arg:
# Parameter: are we passing during the defination of function.
# Argument: are we passing when we call the function.
# def sub(x,y):
#     return x-y
# z=sub(100,50)
# print(z)
#
# def sub(x,y):
#     return x-y
# z=sub(50,100)
# print(z)

# Required Argument:
# def sub(x=100, y=50):
#     return x-y
# z=sub()
# print(z)

# def sub(x=100, y=50):
#     return x-y
# z=sub(200,500)
# print(z)

# def sub(x=100, y=50):
#     return x-y
# z=sub(800)
# print(z)


#Keyword arg:
def sub(x=10,y=20):
    return x-y
z=sub(y=100,x=1000)
print(z)