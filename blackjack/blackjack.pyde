from cards import Card
from player import Player, fontsize
from dealer import Dealer

cardsFull = []
deck = []
player = None
backgroundImage = None
dealer = None
players = []
currentPlayer = None

def setup():
    global player, dealer, backgroundImage, players
    fullScreen()
    textSize(20)
    setupCards()
    player = Player((width / 2 - 100, height - 200), 500)
    dealer = Dealer((width / 2 - 100, 200))
    players = [player, dealer]
    backgroundImage = loadImage('table.png')
    backgroundImage.resize(width, height)
    myFont = createFont("Georgia", 30)
    textFont(myFont)

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

def dealToPlayers():
    global deck, players
    for i in range(2*len(players)):
        player = players.pop(0)
        player.cards = deck[:2]
        deck = deck[2:]
        players.append(player)
    
def hitPlayer():
    global deck, player
    player.cards.append(deck.pop())
    
def hitDealer():
    global deck, dealer
    if(dealer.handValue() < 17):
        dealer.cards.append(deck.pop())

def playOneGame():
    global players, deck, dealer
    for i in range(len(players)):
        player = players.pop()
        player.takeTurn(deck)
        players.append(player)

def bestScore():
    global players
    return max([player.handRank() for player in players[:-1]])

def keyPressed():
    global players, dealer, deck, currentPlayer
    if currentPlayer is not None:
        player = players[currentPlayer]
        if player.isBust() or player.handValue() == 21 or key == 's':
            currentPlayer += 1
            if currentPlayer == len(players):
                currentPlayer = None
                return
            player = players[currentPlayer]
        if key == 'h':
            player.cards.append(deck.pop())
            if player.isBust() or player.handValue() == 21:
                currentPlayer += 1
                if currentPlayer == len(players):
                    currentPlayer = None
                    return
    elif key == 's':
        shuffleDeck()
        dealToPlayers()
        currentPlayer = 0
        
def draw():
    global player, dealer, backgroundImage
    background(backgroundImage)
    player.display()
    dealer.display()
