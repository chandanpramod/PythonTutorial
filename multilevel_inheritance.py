class move:
    def movefw(self):
        print("Move Forword")
    def moveback(self):
        print("Move Backword")
class jump(move):
    def jumpup(self):
        print("Jump up")
    def jumpdown(self):
        print("Jump down")

class mickey(jump):
    def mickey_move(self):
        print("Im mickey moving")

    def mickey_jump(self):
        print("Im mickey jumping")
m=mickey()
m.movefw()
m.moveback()
m.jumpup()
m.jumpdown()
m.mickey_move()
print(mickey.mro())