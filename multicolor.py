import turtle

def draw_multicolor_squares(animal,size):
    for color in ['red','blue','green','purple']:
        animal.color(color)
        animal.forward(size)
        animal.left(90)
    window=turtle.Screen()
    window.bgcolor("blue")
    window.title("multicolor square")
    demo=turtle.Turtle()
    demo.pensize(4) 
    size=20
    for _ in range(15):
        draw_multicolor_squares(demo,size)
        size+=10
        demo.forward(20)
        demo.left(16)
    window.mainloop()