"""
Turtle graphics
https://docs.python.org/3/library/turtle.html

Python har ett paket med inbyggda, enkla funktioner för grafik: turtle. Tänk dig att du har en robotarm som håller en penna mot ett papper. Man kan ge olika instruktioner till roboten, för att styra den. Några exempel:
forward - gå rakt framåt i standardriktningen (peka ursprungligen åt höger)
backward - gå bakåt
left, right - sväng vänster eller höger ett antal grader, 360 grader för ett helt varv
dot - sätt ut en prick med en viss storlek
speed - normal=6, fast=10, maximal=0

Läs mer här: Turtle graphics — Python 3.13.1 documentation
Kodexempel:
import turtle as t

# Upprepa 3 gånger
for x in range(3):
    t.forward(100)
    t.left(120)

# Lyft pennan för att flytta utan att rita
t.penup()
t.forward(200)
t.pendown()
t.dot(10, "red")
t.color("blue"
t.forward(50)

# Låt fönstret stanna kvar tills användaren stänger det
t.mainloop()

1 Skriv en funktion som ritar en kvadrat. Längden på sidan ska vara en parameter till funktionen.

2 Skriv en funktion som flyttar pennan ett lämpligt avstånd till höger, utan att rita. Tanken är att du ska kunna kombinera den med kvadratfunktionen, för att rita flera kvadrater. Exempel:
for x in range(5):
    t.square()
    t.move_next()

3 Bygg om koden så att den ingår i en funktion, som ritar en komplett cirkel. Använd parametrar i stället för värdena 7, 40 och 30.
Tips 1: vad händer om man varierar värdet på range?
Tips 2: 360 grader motsvarar ett helt varv.
for x in range(7):
    t.forward(40)
    t.right(30)

4 Skriv funktioner som ritar de enskilda bokstäverna i ordet "PYTHON" med turtle-modulen. Kombinera dem och försök få bokstäverna att ritas med samma storlek, på en rak linje.


Bonusuppgift, lär dig rekursiva funktioner med turtle graphics:
Python Turtle Meets Fractal Art: A Recursive Journey

"""
import turtle as t

# _______________________ Uppgift 1 _______________________
# 1 Skriv en funktion som ritar en kvadrat.
# Längden på sidan ska vara en parameter till funktionen.

def square(sides, angle=90):
    t.pendown()
    for x in range(4):
        t.left(angle)
        t.forward(sides)
#square(50)

# _______________________ Uppgift 2 _______________________
# Skriv en funktion som flyttar pennan ett lämpligt avstånd till höger, utan att rita.
# Tanken är att du ska kunna kombinera den med kvadratfunktionen, för att rita flera kvadrater.
# Exempel:
# for x in range(5):
#     t.square()
#     t.move_next()
"""
def move_horizontal(length):
        t.penup()
        t.forward(length)

move_horizontal(-300)
for x in range(4):
    move_horizontal(100)
    square(50)

for x in range(10):
    t.forward(40)
    t.right(40)
"""
# _______________________ Uppgift 3 _______________________
#Bygg om koden så att den ingår i en funktion, som ritar en komplett cirkel.
# Använd parametrar i stället för värdena 7, 40 och 30.

def square(sides, angle=90):
    t.pendown()
    for x in range(4):
        t.left(angle)
        t.forward(sides)

def move(length):
    t.penup()
    t.forward(length)
    t.pendown()

move(-150)

for x in range(2):
    move(150)
    square(50)

move(-50)
t.left(90)
move(-50)
t.pendown()
# Full cirkel 360 grader, om right är 10 vrider sig pennan 10 grader varje gång.
# alltså krävs det 36 iterationer för en full cirkel.

t.home()

for x in range(90):
    t.forward(5)
    t.right(4)

# Låt fönstret stanna kvar tills användaren stänger det
t.mainloop()

