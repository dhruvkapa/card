# Lab 4
# Author: Dhruv Kapadia
# Email: dhruvkapadia01@hotmail.com
# Student ID: 215515281

from random import randint

#Draw two cards and check which one has the higher value using if statements
#Create a variable called cards and initialize it to the respective card values
#Return the cards from the variable cards

def drawcards():
    firstCard = randint(2,14)
    secondCard = randint(2,14)

    if firstCard > secondCard:
        cards = [firstCard,secondCard]

    elif firstCard < secondCard:
        cards = [secondCard, firstCard]
    else:
        cards = [firstCard, secondCard]
    return cards


#Define a function called cards2str(card), which will take a parameter called card
#Iterate over the card parameter and check the value of the cards
#If the card value is <= 10, then make the card value into a string
#If the card value is > 10, then make the card value into J, Q , K , or A depending on the card value

def cards2str(card):
    i = 0
    while i < 2:
        if card[i] <= 10:
            card[i] = str(card[i])
        elif card[i] > 10:
            if card[i] == 11:
                card[i] = 'J'
            if card[i] == 12:
                card[i] = 'Q'
            if card[i] == 13:
                card[i] = 'K'
            if card[i] == 14:
                card[i] = 'A'
        i+=1

    return card

#Print out the card values that we got from cards2str(drawcards())
def printhand(humanCards,computerCards):
    cardsHuman = ""
    cardsComputer = ""
    for card in humanCards:

        cardsHuman += card
    for card in computerCards:

        cardsComputer += card


    return cardsHuman, cardsComputer


#Change the cards from printhand() into a list so we can iterate over it
listOfCards = list(printhand(cards2str(drawcards()),cards2str(drawcards())))


#Make the cards that we got from printhand() into two separate lists and so we set two separate variables: listOfCards[0] and listOfCards[1]
humanCards = listOfCards[0]
computerCards = listOfCards[1]

#Iterate over both lists and add the '[]' after each card
firstHand =  ""
secondHand = ""
i = 0
#Iterate over humanCards list and add the '[]' after each card
while i < len(humanCards):

    firstHand += '[' + humanCards[i] + ']'
    if i == len(humanCards)-1:

        firstHand += " YOUR CARDS"
    i+=1

j = 0

#Iterate over computerCards list and add the '[]' after each card
while j < len(computerCards):

    secondHand += '[' + computerCards[j] + ']'
    if j == len(computerCards)-1:
        secondHand += " COMPUTER'S CARDS"

    j+=1

#Since the iteration will go over every card value, the value of 10 will become [1][0] and so we will need to correct that
#Change any values of the iteration that was just performed which are [1][0] into [10] and label that finalHumanCards, and finalComputerCards
finalHumanCards = firstHand.replace("[1][0]", "[10]")
finalComputerCards = secondHand.replace("[1][0]", "[10]")

#This will print out the correct cards along with the '[]' around the card value
print(finalHumanCards)
print(finalComputerCards)



#First check if there is a pair:
# If there is then the one with the pair wins
# If there isn't then check to see who has the highest card
# If first card is highest move on to the second
def printoutcome(checkHumanCards,checkComputerCards):
    #Check if there is a pair with the user's cards
    for element in checkHumanCards:
        for secondElement in checkComputerCards:
            if checkHumanCards.count(str(element)) == 2 and checkComputerCards.count(str(secondElement)) != 2:
                print("YOU WIN")
            # Check if there is a pair with the computer's cards
            elif checkComputerCards.count(str(secondElement)) == 2 and checkHumanCards.count(str(element)) != 2:
                print("YOU LOSE")
            elif checkHumanCards.count(str(element)) != 2 and checkComputerCards.count(str(secondElement)) != 2:
                #If no pair in either, now we go through each element and figure out which is highest card
                for i in checkHumanCards:
                    for j in checkComputerCards:
                        if j == "J":
                            j = 11
                        if j == "Q":
                            j = 12
                        if j == "K":
                            j = 13
                        if j == "A":
                            j = 14
                    if i == "J":
                        i = 11
                    if i == "Q":
                        i = 12
                    if i == "K":
                        i = 13
                    if i == "A":
                        i = 14

        if int(i) > int(j):
            print("YOU WIN")
            break
        elif int(i) < int(j):
            print("YOU LOSE")
            break
        break












    #humanCards and computerCards


print(printoutcome(humanCards,computerCards))
"""    for element in checkHumanCards:
        for secondElement in checkComputerCards:

            if checkComputerCards.count(str(secondElement)) == 2:
                print("YOU LOSE")
            break
        if checkHumanCards.count(str(element)) == 2:
            print("YOU WIN")



        break"""