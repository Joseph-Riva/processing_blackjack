from cards import Card, valueToFace, faceToValue
from player import Player
cardsFull = []
deck = []
player = Player((300, 200), 500)

def setup():
    global player
    fullScreen()
    setupCards()

def setupCards():
    global cardsFull
    cardsFull = []
    for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
        for suit in ['C', 'D', 'H', 'S']:
            cardsFull.append(Card(value, suit))

def shuffleDeck():
    global deck
    deck = cardsFull[:]
    shuffle(deck)

def shuffle(arr):
    for i in range(len(arr)):
        swapIdx = int(random(0, len(arr)))
        arr[i], arr[swapIdx] = arr[swapIdx], arr[i]

def dealToPlayer(player):
    global deck
    shuffleDeck()
    player.cards = deck[:2]
    deck = deck[2:]

def keyPressed():
    global player
    dealToPlayer(player)

def draw():
    global player
    player.display()
