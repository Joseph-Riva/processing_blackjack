from cards import Card
from player import Player, fontsize
cardsFull = []
deck = []
player = None
backgroundImage = None

def setup():
    global player, backgroundImage
    size(1920, 955)
    textSize(20)
    setupCards()
    player = Player((width / 2 - 100, height - 200), 500)
    dealToPlayer()
    backgroundImage = loadImage('table.png')
    backgroundImage.resize(width, height)

def setupCards():
    global cardsFull
    cardsFull = []
    for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
        for suit in ['C', 'D', 'H', 'S']:
            cardsFull.append(Card(value, suit))

def shuffleDeck():
    global deck
    deck = cardsFull[:]
    for i in range(len(deck)):
        swapIdx = int(random(0, len(deck)))
        deck[i], deck[swapIdx] = deck[swapIdx], deck[i]
        
def dealToPlayer():
    global deck, player
    shuffleDeck()
    player.cards = deck[:2]
    deck = deck[2:]
    
def hitPlayer():
    global deck, player
    player.cards.append(deck.pop())
    
def keyPressed():
    global player
    if key == 'h':
        hitPlayer()
    else:
        dealToPlayer()
        
def draw():
    global player, backgroundImage
    background(backgroundImage)
    player.display()
