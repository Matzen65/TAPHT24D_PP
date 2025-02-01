
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
import time
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

    #print(f' {spelare}  summa är "{player_sum}"')

    player_sum = 0
    player_game = True
    computer_sum = 0        #Dealers summa
    dealer_game = True
    limit = 17
    i = 0
    spelare = input("Ange ditt namn tack: ")
    print("Gräns för när Dealern väljer att stanna är satt vid 17")
    print()


    while (player_game or dealer_game):
        i += 1
        print()
        print()
        print(f" ############## GIV: {i} ##############")
        print()
        # Datorn drar första kortet

        if dealer_game:
            print(" **** Dealer ****")
            # Dealer beslutar om att fortsätta eller att stanna
            print(f" Dealerns summa är: {computer_sum}")
            if computer_sum < limit:
                dealers_card = draw(computer_sum) #Dealer drar nytt kort och visar upp det
                computer_sum += dealers_card
                print(f" Dealer drar nytt kort och vänder upp valören: {dealers_card}")
                print(f" Dealerns summa är nu {computer_sum}")
                time.sleep(3)
                if computer_sum > 21:
                    print(f" Dealer är tjock med summan {computer_sum} ")
                    print()
                    time.sleep(1)
                    print(f' {spelare}  summa är {player_sum}')
                    time.sleep(1)
                    print(f'******* Dealer har vunnit *******')
                    print()
                    print("******* Game Over *******")
                    print()
                    break
                print()
            elif computer_sum >= limit:
                print(f" Dealern har {computer_sum} och väljer att stanna!")
                if player_game != True:
                    time.sleep(1)
                    print(f'******* {spelare}  har vunnit *******')
                    print()
                    print("******* Game Over *******")
                    break
                else:
                    dealer_game = False



        if player_game:
            print(f'**** {spelare} ****')
            print(f" {spelare} summa är: {player_sum}")
            answer = input(" Vill du dra nytt kort? [Ja/Nej]: ")
            if answer.casefold() == "ja" or answer.casefold() == "j":
                player_card = draw(player_sum)
                player_sum += player_card
                print(f" {spelare} drar nytt kort och vänder upp valören: {player_card}")
                print(f" {spelare} summa är nu: {player_sum}")
                time.sleep(3)
                if player_sum > 21:
                    print()
                    print(f' Kortets valör är "{player_card}", summan är "{player_sum}" du är tjock och har förlorat')
                    time.sleep(1)
                    print(f" Dealerns summa är: {computer_sum}, dealern har vunnit")
                    print()
                    time.sleep(1)
                    print("******* Game Over *******")
                    print()

            elif answer.casefold() == "nej" or answer.casefold() == "n":
                print()
                print(f" {spelare} väljer att stanna vid summan!: {player_sum}")
                player_game = False





