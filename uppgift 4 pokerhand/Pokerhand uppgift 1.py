

#_______________________ Uppgift 1 _______________________
# 1 Bygg en funktion som slumpar ett spelkort.
# Den ska returnera en lista med två element: färg och valör.
# Färg kan vara: ruter, hjärter, spader eller klöver. Valör kan vara tvåa till ess,
# för enkelhets skull använder vi talen 2 till 14.
# Exempel på ett kort: ["hjärter", 12]

import random
from typing import Tuple, Any

# definiera listor med färg och valör
suits = ["Diamonds", "Spades", "Hearts", "Clubs"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
#list = []

# funktion som utser slumvist kort ut listorna
def pick_a_card(suits, values):
    suit = random.choices(suits)
    value = random.choices(values)
    # returning the selected card
    return suit,value

list = (pick_a_card(suits,values))
print(list)