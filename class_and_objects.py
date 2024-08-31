class ROI: #---Class

    def __init__(self, name, loan,intrest): #---instance class
        self.name=name #---instance variables
        self.loan=loan #---instance variables
        self.intrest=intrest #---instance variables
    def cal_intrest(self):
        return self.loan*self.intrest
P1=ROI('Pramod', 70000000, 0.09) #---Objects
P1_Intrest=P1.cal_intrest()
print(P1_Intrest)

P2=ROI('Abhi', 10000000, 0.04) #---Objects
P2_Intrest=P2.cal_intrest()
print(P2_Intrest)

