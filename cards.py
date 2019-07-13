class Cards():
  ranks=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
  suits=["♥","♦","♣","♠"]

  #use this to create a deck
  def __init__(self):
    self.deck=self.createDeck()

  #this method is used to create a list of cards
  def createDeck(self):
    deck=[]
    for rank in self.ranks:
      for suit in self.suits:
        deck.append((rank,suit))
    return deck

  #this method returns the top card
  def draw(self):
    import random
    if self.deck != []:
      return self.deck.pop(0)
    else:
      print("empty deck")

  def shuffle(self):
    import random
    random.shuffle(self.deck)