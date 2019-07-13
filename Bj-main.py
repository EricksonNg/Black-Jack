#From random file (premade by python) to get randint function
from random import *
# From cards.py file to get "Cards" class
from cards import Cards
#From os file to get system function
from os import system
#From time file to get sleep function
from time import sleep

#Gives each card a value from its rank
values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':0}
print("Game of Black Jack")
sleep(2)

#Draws cards for both player and dealer (draw function from cards.py) 
def deal():
  for i in range(2):
    player_card.append(Deck.draw())
    dealer_card.append(Deck.draw())

#Shows the player's 2 cards in the console while only showing the dealer's second card
def display(): 
  print("Player Hand:", player_card)
  temp = []
  for i in range(1,len(dealer_card)):
    temp.append(dealer_card[i])
  print("Dealer Hand:","[X],", temp)
  print("Player Hand Total:", getvalues(player_card))

def getvalues(cards):
  """gets current value of hand
    input: cards -> a list of tuples
    output: a number that represents the value of your hand 
    """
  total=0
  ace= False
  for card in cards:
    if card[0]=="A":
      ace=True
    else:
      total= total + values[card[0]] 
  if ace:
    if total+11<=21:
      total=total+11
    else:
      total=total+1 
  return total

decision = "1"

while decision == "1":
  #Game Logic
  system('clear')
  Deck= Cards()
  Deck.shuffle()

  dealer_card = []
  player_card = []

  deal()
  display()

  #player's turn
  while getvalues(player_card)<21:
    hit_or_stay = input("1 for hit or 2 for stay")
    if hit_or_stay == "1":
      player_card.append(Deck.draw())
      display()
    else:
      break

  #dealer's turn
  while getvalues(dealer_card)<21:
    difference= abs(21-getvalues(dealer_card))
    if difference>=10:
      hit_or_stay= ["hit"]
    else:
      hit= round(difference/13,2)
      stay=round((13-difference)/13,2)
      hit_or_stay= choices(["hit","stay"],[hit,stay],k=1)
      # print("here is hit_or_stay",hit_or_stay)
    if hit_or_stay== ["hit"]:
      print("\n","The dealer chose to hit","\n")
      dealer_card.append(Deck.draw())
      display()
    else:
      print("\n", "The dealer chose to stay", "\n")
      break

  print("\n", "Final Hands:", "\n", "Dealer Hand:", dealer_card, "\n", "Player Hand:",player_card, "\n")

  #if both get over 21
  if getvalues(player_card)>21 and getvalues(dealer_card)>21:
    print("\n", "You and dealer both got over 21! You both lost!")

  #if player gets over 21 but the dealer doesn't
  elif getvalues(player_card)>21:
    print("\n", "The dealer got {}, while you have over 21 at a value of {}! You lost!".format(getvalues(dealer_card),getvalues(player_card)))

  #if dealer gets over 21 but the player doesn't
  elif getvalues(dealer_card)>21:
    print("\n", "The dealer got over 21 at a value of {}, while you got {}. You won!".format(getvalues(dealer_card),getvalues(player_card)))

  #if both are under 21
  elif getvalues(dealer_card)<=21 and getvalues(player_card)<=21:
    if getvalues(dealer_card)>getvalues(player_card):
      print("\n", "The dealer is closer to 21 at a value of {}, while you only have {}. You lost!".format(getvalues(dealer_card),getvalues(player_card)))
    elif getvalues(dealer_card)<getvalues(player_card):
      print("\n", "You are closer to 21 at a value of {}, while the dealer only has {}. You won! ".format(getvalues(player_card),getvalues(dealer_card)))
  #if both are the same
    elif getvalues(dealer_card)==getvalues(player_card):
      print("\n", "You and the dealer both got the value of {}. It's a tie!".format(getvalues(player_card)))

  print("\n")
  decision=input("If you want play again, press 1. If you want to leave the game, press 2.")





  




