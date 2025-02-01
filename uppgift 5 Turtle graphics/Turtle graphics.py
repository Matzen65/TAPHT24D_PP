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

2 Skriv en funktion som flyttar pennan ett lämpligt avstånd till höger, utan att rita.
Tanken är att du ska kunna kombinera den med kvadratfunktionen, för att rita flera kvadrater. Exempel:
for x in range(5):
    t.square()
    t.move_next()

3 Bygg om koden så att den ingår i en funktion, som ritar en komplett cirkel. Använd parametrar i stället för värdena 7, 40 och 30.
Tips 1: vad händer om man varierar värdet på range?
Tips 2: 360 grader motsvarar ett helt varv.
for x in range(7):
    t.forward(40)
    t.right(30)

4 Skriv funktioner som ritar de enskilda bokstäverna i ordet "PYTHON" med turtle-modulen.
Kombinera dem och försök få bokstäverna att ritas med samma storlek, på en rak linje.

Bonusuppgift, lär dig rekursiva funktioner med turtle graphics:
Python Turtle Meets Fractal Art: A Recursive Journey

"""
import turtle as t

print()
version = int(input("ange vilken version som önskas av 1, 2, 3, 4: "))
print()

# _______________________ Uppgift 1 _______________________
# 1 Skriv en funktion som ritar en kvadrat.
# Längden på sidan ska vara en parameter till funktionen.

# funktion som ritar en kvadrat.
# Man anger centrumpunkten och hur den ska luta samt sidornas längd
# pendown kommer sedan att börja rita från kvadratens övre vänstra hörn
# funktionen avslutar med att återgå till startpunkten och riktad rakt åt höger.


if version == 1:
    def square1(x,y,sides, angle):
        t.penup()
        t.home()
        t.forward(-sides/2)
        t.left(90)
        t.forward(sides/2)
        t.pendown()
        for i in range(4):
            t.right(angle)
            t.forward(sides)
        t.penup()
        t.home()

    square1(0,0,100, 90)

# _______________________ Uppgift 2 _______________________
# Skriv en funktion som flyttar pennan ett lämpligt avstånd till höger, utan att rita.
# Tanken är att du ska kunna kombinera den med kvadratfunktionen, för att rita flera kvadrater.
# Exempel:
# for x in range(5):
#     t.square()
#     t.move_next()

if version == 2:
    t.speed('fast')
    def square2(x, y, side, tilt):
        # t.pos = kvadrats centrumpunkt är (x,y)
        t.up()
        t.goto(x,y)  # söker upp önskad centrumpunkt (x,y):
        #print("startpunkt ", t.pos())
        t.right(tilt)  # vrider markören i tiltat läge medurs
        #söker upp kvadratens övre vänstra hörn
        t.fd(-side/2)
        t.left(90)
        t.fd(side/2)
        t.right(90)
        t.down()
        #print("sätter ner pennan på: ",t.pos())
        for i in range(4):
            t.forward(side)
            t.right(90)
        t.up()
        t.left(tilt)
        t.home()
        #t.goto(x,y) # återgår till startpunkten (x,y):
        #print("slutpunkt ",t.pos()) #återgår till startpunkten:

    t.home()
    square2(-100,100, 50, 45)
    square2(100,100,50, 45)
    square2(-100,-100,50, 45)
    square2(100,-100,50, 45)



# _______________________ Uppgift 3 _______________________
#Bygg om koden så att den ingår i en funktion, som ritar en komplett cirkel.
# Använd parametrar i stället för värdena 7, 40 och 30.

# Full cirkel 360 grader, om right är 10 vrider sig pennan 10 grader varje gång.
# alltså krävs det 36 iterationer för en full cirkel.

if version == 3:
    t.speed('fast')
    def circle(i, f, ri):
        for x in range(i):
            t.fd(f)
            t.right(ri)

    grader = 10
    full_c = int(360/grader)
    #t.goto(-4,27)
    t.down()
    circle(full_c,20,grader)

    # Låt fönstret stanna kvar tills användaren stänger det
    t.mainloop()

if version == 4:
    """
    # _______________________ Uppgift 4 _______________________
    # Skriv funktioner som ritar de enskilda bokstäverna i ordet "PYTHON" med turtle-modulen. 
    # Kombinera dem och försök få bokstäverna att ritas med samma storlek, på en rak linje.
    t.seth(0) setheading = 0 
    t.left(45)  turn 45 degree left
    t.right(45)  turn 45 degree right
    t.forward() t.fd()     Go forward
    t.back()        go backward
    t.up() lift pen
    t.down() pendown
    """

def bokstav_P():
    t.seth(0)
    t.left(90)
    t.fd(100)
    t.right(90)
    t.fd(20)
    t.circle(-25, 180)
    t.fd(20)

def bokstav_Y(r_angle, l_angle, length):
    t.seth(0)
    t.left(90)
    t.fd(60)
    t.right(r_angle)
    t.fd(length)
    t.up()
    t.backward(length)
    t.left(2*l_angle)
    t.down()
    t.fd(55)

def bokstav_T():
    t.seth(0)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(40)
    t.back(80)

def bokstav_H():
    t.seth(0)
    t.left(90)
    t.down()
    t.fd(100)
    t.up()
    t.back(50)
    t.down()
    t.right(90)
    t.fd(50)
    t.left(90)
    t.up()
    t.fd(50)
    t.down()
    t.right(180)
    t.fd(100)

def bokstav_O():
    t.seth(0)
    t.left(180)
    t.circle(-25, 90)
    t.fd(50)
    t.circle(-25, 180)
    t.fd(50)
    t.circle(-25, 90)

def bokstav_N():
    t.seth(0)
    t.left(90)
    t.fd(100)
    t.right(155)
    t.fd(110)
    print(t.pos())
    t.left(155)
    t.fd(100)

t.speed('fast')

# flytta startpunkt för respektive bokstav, default i vänstra delen av fönstret
def starting_point(x=-200, y=0, x_down=0, y_down=0):
    t.up()
    t.setpos(x + x_down, y + y_down)
    t.down()


starting_point()
bokstav_P()

starting_point(x_down=100)
bokstav_Y(45,45,55)

starting_point(x_down=190)
bokstav_T()

starting_point(x_down=250)
bokstav_H()

starting_point(x_down=365)
bokstav_O()

starting_point(x_down=420)
bokstav_N()

t.mainloop()


