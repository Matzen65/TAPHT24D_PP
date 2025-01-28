import module1
import module2
import module3
import module4
import module5
import module6
import module7
import module8

print(" 1. ----------------------------------------------------")
# 1 Skriv en funktion som tar en sträng som parameter.
# När den anropas ska den skriva ut strängen och "är en fena på programmering".
# Exempel:
# my_function("David") → "David är en riktig hacker"

module1.my_function("David")


print(" 2a. ----------------------------------------------------")
# 2a Skriv en funktion med namnet "eko".
# När den anropas med en sträng ska den upprepa strängen, och skriva ut resultatet.
# Exempel:
# eko("hej") → skriver ut "hejhej"

module2.eko("hej")


print(" 2b. ----------------------------------------------------")
# 2b Lägg till en parameter "count", som avgör hur många ekon som ska skapas.
# Exempel:
# eko("hej", 3) → skriver ut "hejhejhej"

module2.eko("hej", 3)


print(" 3. ----------------------------------------------------")
# 3 Följande kod ska sluta loopa efter 5 varv.
# Flytta den in i en funktion och justera den enligt kommentaren.

# end = 5
# y = 1
# for x in range(1, 100):
#     y *= 2
#     # avsluta loopen med en if-sats här
# print(y)

module3.break_loop()


print(" 4. ----------------------------------------------------")
# 4 Skriv en funktion med namnet last.
# Den ska ta en lista som parameter och returnera det sista elementet i listan.
# last([1, 2, 3]) → 3

print(module4.last([1, 2, 3]))
print(module4.last([1, 2, 5, 6]))


print(" 5. ----------------------------------------------------")
# 5 Skriv en funktion med namnet cut_edges.
# Den ska ta en lista som parameter. När den anropas ska den returnera en ny lista,
# där den har tagit bort första och sista elementet.
# cut_edges([1, 2, 3, 4]) → [2, 3]

print(module5.cut_edges([1,2,3]))
print(module5.cut_edges([1,2,5,6]))


print(" 6. ----------------------------------------------------")
# 6 Lös felen i koden.

# def increase(x):
#     return x
#     x += 1
# print(increase(1))

print(module6.increase(1))


print(" 7 ----------------------------------------------------")
# 7 Bygg en funktion med namnet average.
# Den ska ta parametrar: x och y. Båda ska vara tal.
# Funktionen ska returnera medelvärdet.
# Till exempel så räknar man ut medelvärdet av 4 och 8
# genom med formeln: (4 + 8) / 2, vilket blir 6.
# Tips: det kan vara enklare att använda fler variabler.

print(module7.average(4,8))


print(" 8. ----------------------------------------------------")
# 8 Gör en funktion som kan skriva ut innehållet i en lista lite snyggare.
# Först ska funktionen tala om ifall listan är tom, eller hur många element den har.
# Sedan ska funktionen skriva ut elementen i en punktlista.
# Exempel:
# pretty_print(["a", "b", 3.14])
# Listan har 3 element:
# 1. a
# 2. b
# 3. 3.14

module8.pretty_print([])
module8.pretty_print(["a", "b", 3.14])

