# Variable scope in Python - boundary of variables within a program
#
# Local Scope
#
# Global Scope
#
# global keyword
#
# LEGB rule: Local -> Enclosing -> Global -> Built-in

# def var_loc():
#     x = 10
#     print(x)
#
# var_loc()
#
# x=10
# def var_glob():
#     print(x)
# var_glob()

# def glob_key():
#     global x
#     x=10
#     print(x)
# glob_key()
#
# def glob_loc():
#     print(x)
# glob_loc()

# def var():
#     x=10
#     print(x)
#     def var_enc():
#         print(x)
#         def child():
#             print(x)
#         child()
#     var_enc()
# var()


x=100
def father():
    x=10
    print(x)
    def son():
        x=20
        print(x)
        def grandson():
            # x=30
            print(x)
            def greater_grandson():
                # global x
                # x=40
                print(x)
            greater_grandson()
        grandson()
    son()
father()
