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
georgiaFont = None

temporaryDraw = []

def setup():
    global player, dealer, backgroundImage, players, georgiaFont
    fullScreen()
    textSize(20)
    setupCards()
    player = Player((width / 2 - 100, height - 200), 500)
    dealer = Dealer((width / 2 - 100, 200))
    players = [player, dealer]
    backgroundImage = loadImage('table.png')
    backgroundImage.resize(width, height)
    georgiaFont = createFont("Georgia", 30)
    textFont(georgiaFont)

def setupCards():
    global cardsFull
    global myClients
    myClients = []
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
    global deck, players, dealer, temporaryDraw
    dealer.cardRevealed = False
    for i in range(2*len(players)):
        player = players.pop(0)
        player.cards = deck[:2]
        deck = deck[2:]
        players.append(player)
    for player in players:
        if player.handRank() == 22:
            if player is dealer:
                dealer.cardRevealed = True
            temporaryDraw.append({'draw': drawBlackjack, 'time': int(frameRate*2)})
            
def drawBlackjack():
    boxW = 200
    boxH = 100
    fill(255)
    rect(width/2-40, height/2, boxW, boxH, 7)
    fill(255, 40, 40)
    textAlign(CENTER, CENTER)
    text("Blackjack!", width/2-40, height/2, boxW, boxH)
    textAlign(BASELINE, BASELINE)
    
def drawBust():
    boxW = 200
    boxH = 100
    fill(255)
    rect(width/2-40, height/2, boxW, boxH, 7)
    fill(255, 40, 40)
    textAlign(CENTER, CENTER)
    text("Bust!", width/2-40, height/2, boxW, boxH)
    textAlign(BASELINE, BASELINE)
    
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
                if player.isBust():
                    temporaryDraw.append({'draw': drawBust, 'time': int(2*frameRate)})
                currentPlayer += 1
                if currentPlayer == len(players):
                    currentPlayer = None

    elif key == 's':
        shuffleDeck()
        dealToPlayers()
        currentPlayer = 0
        
def drawIntroScreen():
    global currentPlayer, georgiaFont, temporaryDraw
    if currentPlayer is None and not temporaryDraw:
        textSize(50)
        fill(0)
        textAlign(CENTER)
        text("Blackjack!", width // 2, 200)
        textSize(30)
        text("To start a game, press 'S'", width //2, 500)
        textAlign(BASELINE)
        textFont(georgiaFont)
        
def draw():
    load()
    global player, dealer, backgroundImage, temporaryDraw
    background(backgroundImage)
    drawIntroScreen()
    if currentPlayer is not None or temporaryDraw:
        player.display()
        dealer.display()
    for i in range(len(temporaryDraw) - 1,-1,-1):
        obj = temporaryDraw[i]
        obj['time'] -= 1
        if not obj['time']:
            temporaryDraw.pop(i)
        obj['draw']()
        
add_library('net')
myClient = None
        
def load():
    global myClients
    myClients.append(Client(this, "localhost", 5000))
    myClients[-1].write("GET / HTTP/1.1\r\n")
    myClients[-1].write("\r\n")
    if(myClients[0].available() > 0):
        dataIn = myClients[0].readString()
        if('[]' not in dataIn):
            try:
                value = dataIn[dataIn.index('[') + 1:-1]
                if (int(value) == 1):
                    player.cards.append(deck.pop())
                    if player.isBust() or player.handValue() == 21:
                        currentPlayer += 1
                        if currentPlayer == len(players):
                            currentPlayer = None
                if(int(value) == 2):
                    print("here")
                    currentPlayer += 1
                    if currentPlayer == len(players):
                        currentPlayer = None
                return
            except:
                pass
        myClients.pop(0)
