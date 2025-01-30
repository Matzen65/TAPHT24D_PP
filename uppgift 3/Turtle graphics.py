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

# _______________________ Uppgift 1 _______________________
# 1 Skriv en funktion som ritar en kvadrat.
# Längden på sidan ska vara en parameter till funktionen.

# funktion som ritar en kvadrat.
# Man anger centrumpunkten och hur den ska luta samt sidornas längd
# pendown kommer sedan att börja rita från kvadratens övre vänstra hörn
# funktionen avslutar med att återgå till startpunkten och riktad rakt åt höger.

"""
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

t.home()
def circle(i, f, ri):
    t.down()
    for x in range(i):
        t.fd(f)
        t.right(ri)

#print("ritar en cirkel")

grader = 10
full_c = int(360/grader)
t.goto(-4,27)
circle(full_c,5,grader)

# Låt fönstret stanna kvar tills användaren stänger det
t.mainloop()

# _______________________ Uppgift 4 _______________________
#Skriv funktioner som ritar de enskilda bokstäverna i ordet "PYTHON" med turtle-modulen. 
#Kombinera dem och försök få bokstäverna att ritas med samma storlek, på en rak linje.
"""
def bokstav_P(a,b,c):
    t.home()
    t.left(a)
    t.fd(b*1.05)
    t.right(65)
    for x in range(c):
        t.fd(4)
        t.right(10)
    t.up()
    t.home()
    #t.mode()

def bokstav_Y(a,b,c,d):
    #t.home()
    print("start Y",t.pos())
    t.fd(b*1.2)
    t.down()
    t.left(a)
    t.fd(b*1.2)
    t.right(d)
    print(t.pos())
    t.fd(b*0.8)
    print("överst i Y",t.pos())
    t.goto(72,72)
    print(t.pos())
    t.down()
    t.left(d*2)
    t.fd(b*0.8)
    t.up()
    t.home()

def bokstav_H(a,b,c,d):
    #t.home()
    t.fd(b*1.2)
    t.down()
    t.left(a)
    t.fd(b)
    #t.up()
    t.fd(-b/2)
    t.right(a)
    t.fd(b/2)
    t.left(90)
    t.fd(b/2)
    t.right(180)
    t.fd(b)
    t.home()



    #t.home()




bokstav_P(90,100,24)
bokstav_Y(90,60,45,45)
bokstav_H(90,106,0,0)
t.mainloop()



