from cards import Card
cards = []

def setup():
    fullScreen()
    setupCards()

def setupCards():
    global cards
    for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
        for suit in ['C', 'D', 'H', 'S']:
            cards.append(Card(value, suit))
    shuffle(cards)
            
def shuffle(arr):
    for i in range(len(arr)):
        swapIdx = int(random(0, 52))
        cards[i], cards[swapIdx] = cards[swapIdx], cards[i]
        
def keyPressed():
    global cards
    shuffle(cards)
        
def draw():
    global cards
    cards[0].display(0, 0)
