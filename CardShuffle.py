#Name: Talha Mansoor
#NSID: kgy284
#Student Number:11346490
#Course Number: CMPT-145
#Instructor: Jeff Long

import random as r

#class definition
class Card(object):


    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.deck = []
        self.player1=[]

        return
    #create a deck of cards by combining possibilities
    def create(self):
        for val in self.value:
            for su in self.suits:
                x=val+su
                self.deck.append(x)
        return self.deck


    def deal(self,num_cards,num_players,deck):

        """

                    Purpose : To RANDOMLY deal cards out from a deck. The cards will be removed from
                   the deck.
                   PreConditions: number of cards, number of players, deck list
                   post conditions: none
                   Return: List of sublists"""
        players = []

        if len(deck)< num_players * num_cards :
            return print("Too many players.\n","Players:",num_players,'\n' "Cards:",num_cards, "\ndeck",deck )

                          #Randomly choose index for deck and append it to hands
        for x in range(num_players):
            hands = []

            for y in range(num_cards):
                t = r.randint(0, len(deck) - 1)
                hands.append(deck[t])
            players.append(hands)

        return players



Card=Card()
y=Card.create()

print(Card.deal(8,2,y))