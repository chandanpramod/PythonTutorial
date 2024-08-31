class move:
    def __init__(self):
        pass
    def movefwd(self):
        print("Move Fwd")
    def moveback(self):
        print("move back")



class jump:
    def __init__(self):
        pass
    def jumpup(self):
        print("Jump up")
    def jumpdown(self):
        print("Jump down")


class pokemon(move,jump):
    pass
    print("I am pokemon")


# p=pokemon()
# p.movefwd()
# p.moveback()
# p.jumpup()
# p.jumpdown()

class micky(move,jump):
    def movefwd(self):
        print("Im Mickey Moving")
    def jumpup(self):
        print("I am Mickey Jumping up")
m=micky()
m.movefwd()
m.jumpup()
m.moveback()
m.jumpdown()
print(micky.mro())