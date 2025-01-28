
"""
Spelet 21
Om man lägger ihop talen 1 + 2 + 3 + 4 + …  så kommer talens summa att bli större och större.
Förr eller senare kommer man förbi 21. Skriv en funktion som skriver ut det första talet i talserien
som är större än 21.

Version 2: i stället för att använda talserien, slumpa tal mellan 1 och 13. (talen i en vanlig kortlek)
Tips: importera modulen random och använd funktionen randint för att slumpa tal.
Exempel: card = random.randint(1, 13)

Möjlig vidareutveckling: bygg ett spel som frågar användaren om man vill ta ett nytt kort eller stanna.
(slumpa ett tal) Gör så att datorn kan simulera en motståndare. Målet är att vinna över datorn.
"""
#===========================================================

import random
print()
version = int(input("ange vilken version som önskas av 1-3: "))
print()

#--------------------------Version 1--------------------------
# Enbart talserien 1,2,3,4...-21 testas, inga slumptal används.
if version == 1:
    def above_21():
        sum = 0
        for number in range(1, 22):
            sum += number
            #print(sum)
            if sum > 21:
                #print(f'Det första talet som överskrider Summan 21 är "{number}"')
                return number

    result = above_21()
    print(f"Det första talet som överskrider Summan 21 är: {result}")

#--------------------------Version 2--------------------------
# Slumpar fram kort mellan 1och 13

elif version == 2:
    def above_21():
        sum = 0
        for i in range(1, 22):
            card = random.randint(1, 13)
            sum += card
            print(f" Draget kort är: {card}")
            if sum > 21:
                print(f' Kort "{card}" ger summan "{sum}"')
                return card


    result = above_21()
    print()
    print(f' Det senast dragna kortet är: "{result}"')

#--------------------------Version 3--------------------------
# Fråga om man vill dra nytt kort eller stanna

elif version == 3:
    def draw(sum):
        card = random.randint(1, 13)
        sum += card
        return card

    player1_sum = 0
    player1_in_game = True
    computer_sum = 0
    computer_in_game = True
    spelare = input(" Ange ditt namn tack: ")
    print()

    i = 0
    while (player1_in_game or Dealer_in_game): #and (player1_sum <= 21 or computer_sum <= 21):
        i += 1 # räknare för antal spelomgångar
        print(f" ############## GIV: {i} ##############")
        print()
        # Datorn drar första kortet
        Dealer_in_game = True
        player1_in_game = True

        # Dealer (dator)
        if Dealer_in_game:
            print(" **** Dealer ****")
            # Dealer beslutar om att fortsätta eller att stanna
            print(f" Dealerns summa är: {computer_sum}")
            if computer_sum < 21:
                print(" Dealer drar nytt kort!: ")
                dealers_card = draw(computer_sum) #Dealer drar nytt kort och visar upp det
                computer_sum += dealers_card
                print(f" Dealer vänder upp valören: {dealers_card}")
                if computer_sum > 21:
                    print(f" Dealer är tjock med summan {computer_sum} ")
                    print(f' {spelare}  summa är "{player1_sum}"')
                    print(f'******* {spelare}  har vunnit *******')
                    print()
                    print("******* Game Over *******")
                    print()
                    break
                print()

            elif computer_sum == 21:
                print(" Dealern har 21 och väljer att stanna!")
                Dealer_in_game = False
            #else:


        if player1_in_game:
            print(f'**** {spelare} ****')
            print(f" {spelare} summa är: {player1_sum}")
            answer = input("Vill du dra nytt kort? [Ja/Nej]: ")
            if answer.casefold() == "ja" or answer.casefold() == "j":
                print(f"{spelare} drar nytt kort!")
                player1_card = draw(player1_sum)
                print(f"{spelare} vänder upp valören: {player1_card}")
                player1_sum += player1_card
                if player1_sum > 21:
                    print(f' Kortets valör är "{player1_card}", summan är "{player1_sum}" du är tjock och har förlorat')
                    print(f" Dealerns summa är: {computer_sum}, dealern har vunnit")
                    print()
                    print("******* Game Over *******")
                    print()
                    break
            elif answer.casefold() == "nej" or answer.casefold() == "n":
                print(f" {spelare} väljer att stanna!: {player1_sum}")
                player1_in_game = False




