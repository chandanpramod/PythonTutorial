# class parent:
#     def __init__(self):
#         print("Parent instance method")
#     def parent_money(self):
#         print("Parent Money")
# class child(parent):
#     pass
# P1=parent()
# P1.parent_money()



# class parentclass:
#     def __init__(self):
#         print("Parent Instance")
#
#     def parent_property(self):
#         print("Parent Property")
# class Child_class(parentclass):
#     pass
#
# c1=Child_class()
# c1.parent_property()


class ROI:
    intrest=0.06
    def __init__(self, loan_amount, Name):
        self.loan_amount=loan_amount
        self.Name=Name
    def intrst_cal(self):
        return self.loan_amount*self.intrest

class student(ROI):
    intrest = 0.04
    # pass
s=student(500000,'Pramod')
Stu=s.intrst_cal()
print(Stu)