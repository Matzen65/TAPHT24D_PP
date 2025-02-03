import random


# funktion som returnerar ett random spelkort.
def pick_a_card(suits, values):
    suit = random.choices(suits)
    value = random.choices(values)
    # returning the selected card
    return suit, value

# definiera listor med färg och valör
#suits = ["Diamonds", "Spades", "Hearts", "Clubs"]
#values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

uppgift = int(input("välj en uppgift av 1, 2, 3: "))
#uppgift =3

#_______________________ Uppgift 1 _______________________
# 1 Bygg en funktion som slumpar ett spelkort.
# Den ska returnera en lista med två element: färg och valör.
# Färg kan vara: ruter, hjärter, spader eller klöver. Valör kan vara tvåa till ess,
# för enkelhets skull använder vi talen 2 till 14.
# Exempel på ett kort: ["hjärter", 12]

###################uppgift 1#################################################
if uppgift == 1:
    #import random
    print("-------------------uppgift 1--------------------")
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

######################uppgift 2#################################################
if uppgift == 2:

    # definiera listor med färg och valör
    suits = ["Diamonds", "Spades", "Hearts", "Clubs"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

    # jämför två kort och talar om ifall de har samma valör
    def find_equal_value(card1, card2):
        if card1[1] == card2[1]:
            return card1 == card2

    card1 = (pick_a_card(suits,values))
    print(" The first random card is", card1)
    card2 = (pick_a_card(suits,values))
    print(" The second random card is", card2)
    print()

    if (find_equal_value(card1, card2)):
        print(f' The two cards {card1[1]} and {card2[1]} has the same value')
    else:
        print(f' The two cards {card1[1]} and {card2[1]} dont have the same value')


###################### uppgift 3 #################################################
# bygger en hand om 5 kort samt "undviker dublettkort"
# vilket annars förekommer ungefär var 5e gång
# funktionen talar sedan om man har ett par på hand.
if uppgift == 3:

    def poker_hand(the_hand):
        # build the hand
        while len(the_hand) < 5:
            # kallar på funktion som tar ett random kort rad 20
            new_card = (pick_a_card(suits, values))

            if len(the_hand) > 0:
                # checka om new_card redan finns (dublett)
                duplicate = False
                for card in the_hand:
                    if card == new_card:
                        duplicate = True
                # Om dublett, fortsätt loopa
                if duplicate:
                    continue
            #lägg till kort i handen med 5 kort
            the_hand.append(new_card)
        return the_hand

    def count_equal_values(the_hand):
        #funktionen matas med 5 kort och returnerar antal med lika valör

        # Skapa en lista med bara värden på korten
        values = [item[1] for item in the_hand]
        same_values = []
        for value in values:
            count = 0
            for card in the_hand:
                card_value = card[1]
                if card_value == value:
                    count += 1

            same_values.append(count)

        ind1 = 0
        duplicates = []
        app = 0
        #List the duplicate cards
        for ind in same_values:
            if ind >= 2:
                app = the_hand[ind1]
                duplicates.append(app)
            ind1 += 1

        return duplicates

    # definiera listor med färg och valör
    suits = ["Diamonds", "Spades", "Hearts", "Clubs"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

    #Kallar på funktionen som bygger en random pokerhand fri från dubletter
    the_hand = []
    game_hand = (poker_hand(the_hand))
    for i in range(5):
        print(game_hand[i])

#----------------------------flertal funktion
    # check for pairs in the hand
    #print("equal values ",count_equal_values(game_hand))
    par = []
    par = count_equal_values(game_hand)
    print()
    if par:
        print("the game hand has duplicates in:", par[0], "and", par[1])
    else:
        print("No duplicates was found")



