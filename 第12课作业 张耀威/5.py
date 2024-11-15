import turtle as t
def tree(changdu,fenzhi):
    if(fenzhi<=0):
        return
    t.forward(changdu)
    t.left(30)
    tree(0.8*changdu,fenzhi-1)
    t.right(60)
    tree(0.8*changdu,fenzhi-1)
    t.left(30)
    t.backward(changdu)
    return
t.pensize(4)
t.color("red")
t.left(90)
t.goto(0,-300)
tree(150,5)
