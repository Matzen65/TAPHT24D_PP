# 1.Läsa och förstå kod - diskutera i grupp
# Skriv ner vad du tror kommer skrivas ut.
# Skriv sedan in koden i din IDE, exakt som den står, och kör den.
# Fick du samma resultat som du trodde? Om inte, varför?


print("------------------")
print("uppgift 1.1a")
print()
def foo(t):
    print("test")

foo("hej")

print(f'skriver ut "test" då funktionens parameter heter "t"')

print("------------------")
print("uppgift 1.1b")
print()
def fun1(x, y):
    return x * y

print(3, 5)
print(f'skriver ut "x y" då vi inte kallat på funktionen för x och y')

print("------------------")
print("uppgift 1.1c")
print()
def fun1(x, y):
    return x * y
print(fun1(3, 5))
print(f'skriver ut "15" då vi kallat på funktionen med indata för x och y')

print("------------------")
print("uppgift 1.1d")
print()
def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))
print(a)
print(f'skriver ut "125"...."5*25(5*2+5*3)"')

print("------------------")
print("uppgift 1.1e")
print()
a = 5
def fun3(a):
    a += 1

a += 2
print(a)
print(f'skriver ut "7" då vi inte kallat på funktionen för a')

print("------------------")
print("uppgift 1.1f")
print()
def foo(i):
    #print(2*i*i)
    return 2*i*i

def goo(x, y):
    return x(y)

a = goo(foo, 3);
print(a)
print(f'skriver ut "18" foo returnerar 2*3*3')

print("------------------")
print("uppgift 1.1g")
print()
# Funktionen "isinstance" kan kontrollera en variabels datatyp.
# Vad gör funktionen is_number? Går det att förbättra koden?
def is_number(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    return False

print(is_number(5.5))
print(is_number(42))

print(f'skriver ut "True True" då funktionen kollar om argumenten är int eller float')

print("------------------")
print("uppgift 1.1h")
print()
def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found

aw = average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])
print(aw)
print(f'skriver ut listan med orden "hows, going, coding" '
      f'då de har fler än 4 och mindre än 8 bokstäver "4<ordlängd<8"')

print("------------------")
print("uppgift 1.1i")
print()
# En uppgift i tre delar:
# Lista ut vad som är funktionens syfte, baserad på namn och sammanhang.
# Lista ut vad som ska vara det förväntade resultatet för de tre testlistorna.
# Rätta felen, så funktionen gör det den ska.

def find_min(numbers):
    counter = 0
    for item in numbers:
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11])
find_min([])
find_min([100])


print(f' ny lösning som fungerar nedan, då vi använder None istället för 0 i funktionen')


def find_min(numbers):
    counter = None
    for item in numbers:
        if counter is None:
            counter = item
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11])
find_min([])
find_min([100])

print(f'1. letar upp minsta talet')
print(f'2. -11,0,0')
print(f'3. ny lösning som fungerar ovan, då vi använder None istället för 0 i funktionen')
print("------------------")