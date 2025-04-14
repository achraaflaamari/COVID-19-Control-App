import turtle

# Fonction pour dessiner un cœur
def draw_heart():
    turtle.fillcolor('red')
    turtle.penup()
    turtle.goto(0, -30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(229)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.left(120)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(229)
    turtle.end_fill()

# Fonction pour afficher le texte "Dabdoobty" en rouge
def display_text():
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.color('red')
    turtle.write("Dabdoobty", align='center', font=('Arial', 30, 'bold'))
    turtle.penup()
    turtle.goto(0, -140)
    turtle.pendown()
    turtle.color('red')
    turtle.write("🙄🙄🙄", align='center', font=('Arial', 30, 'bold'))

# Configuration de la fenêtre Turtle
turtle.speed(0)
turtle.bgcolor("white")

# Dessiner le cœur
draw_heart()

# Afficher le texte en rouge
display_text()

# Fermer la fenêtre en cliquant dessus
turtle.exitonclick()
