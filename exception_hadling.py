try:
    # print("Enter numbr1 : ")
    x= int(input("Enter Number 1 : ", ))
    # print("Enter number2 : ")
    y=int (input("Enter Number 2 : "))
    print(x/y)
    if y==0:
        raise Exception("Number/denominator 2 should not be zero")
except Exception as e:
    print("Exception block executed- Error Occure plz try again")

else:
    print("No exception or error in code so Else block executed")
finally:
    print("finally always executed")