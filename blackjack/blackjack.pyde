from cards import Card
from player import Player, fontsize
from dealer import Dealer
from movingCard import MovingCard

cardsFull = []
counter = 0
deck = []
player = None
backgroundImage = None
dealer = None
players = []
currentPlayer = None
georgiaFont = None
faceDownCard = None

temporaryDraw = []
dealerWait = 0

def passFunction():
    pass

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
        deck[i].visible = False
        deck[swapIdx].visible = False
        deck[i], deck[swapIdx] = deck[swapIdx], deck[i]

def dealToPlayers():
    global deck, players, dealer, temporaryDraw
    dealer.cardRevealed = False
    for player in players:
        player.cards = []
    for i in range(2*len(players)):
        giveCard(players[i % len(players)])
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
    
def drawVictory():
    boxW = 200
    boxH = 100
    fill(255)
    rect(width/2-40, height/2, boxW, boxH, 7)
    fill(255, 40, 40)
    textAlign(CENTER, CENTER)
    text("Win!", width/2-40, height/2, boxW, boxH)
    textAlign(BASELINE, BASELINE)
    
def drawDefeat():
    boxW = 200
    boxH = 100
    fill(255)
    rect(width/2-40, height/2, boxW, boxH, 7)
    fill(255, 40, 40)
    textAlign(CENTER, CENTER)
    text("Defeat!", width/2-40, height/2, boxW, boxH)
    textAlign(BASELINE, BASELINE)

def drawPush():
    boxW = 200
    boxH = 100
    fill(255)
    rect(width/2-40, height/2, boxW, boxH, 7)
    fill(255, 40, 40)
    textAlign(CENTER, CENTER)
    text("Push!", width/2-40, height/2, boxW, boxH)
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

def takeDealerTurn():
    global dealer, deck, players, dealerWait, temporaryDraw
    dealerWait -= 1
    if not dealerWait:
        toBeat = max([player.handRank() for player in players if player is not dealer])
        curRank = dealer.handRank()
        if curRank < 17 and curRank > 0 and toBeat > 0 and not toBeat == 22:
            giveCard(dealer)
            for tempDraw in temporaryDraw:
                if tempDraw['draw'] == takeDealerTurn:
                    tempDraw['time'] = int(frameRate*2.51)
                    dealerWait = int(frameRate*2.5)
            if dealer.handRank() == 0:
                temporaryDraw.append({'draw': drawBust, 'time': int(2.5*frameRate)})
        else:
            if curRank == 0:
                temporaryDraw.append({'draw': drawVictory, 'time': int(2.5*frameRate)})
            elif curRank < toBeat:
                temporaryDraw.append({'draw': drawVictory, 'time': int(2.5*frameRate)})
            elif curRank > toBeat:
                temporaryDraw.append({'draw': drawDefeat, 'time': int(2.5*frameRate)})
            else:
                temporaryDraw.append({'draw': drawPush, 'time': int(2.5*frameRate)})

def keyPressed():
    global players, dealer, deck, currentPlayer, dealerWait, temporaryDraw
    if currentPlayer is not None:
        player = players[currentPlayer]
        if player.isBust() or player.handValue() == 21 or key == 's':
            currentPlayer += 1
            if currentPlayer == len(players) - 1:
                temporaryDraw.append({'draw': takeDealerTurn, 'time': int(frameRate*2.51)})
                dealerWait = int(frameRate*2.5)
                dealer.cardRevealed = True
                takeDealerTurn()
                currentPlayer = None
                return
            player = players[currentPlayer]
        if key == 'h':
            giveCard(player)
            if player.isBust() or player.handValue() == 21:
                if player.isBust():
                    temporaryDraw.append({'draw': drawBust, 'time': int(2*frameRate)})
                currentPlayer += 1
                if currentPlayer == len(players) - 1:
                    temporaryDraw.append({'draw': takeDealerTurn, 'time': int(frameRate*2.51)})
                    dealerWait = int(frameRate*2.5)
                    dealer.cardRevealed = True
                    takeDealerTurn()
                    currentPlayer = None
                    return

    elif key == 's':
        temporaryDraw = []
        shuffleDeck()
        dealToPlayers()
        if players[0].handRank() == 22:
            dealerWait = int(frameRate*2.5)
            dealer.cardRevealed = True
            temporaryDraw.append({'draw': takeDealerTurn, 'time': int(frameRate*2.51)})
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

def drawDeck():
    global faceDownCard
    if faceDownCard is None:
        faceDownCard = loadImage('green_back.png')
        aspectRatio = faceDownCard.width/faceDownCard.height
        faceDownCard.resize(100, 100*aspectRatio)
    aspectRatio = faceDownCard.width/faceDownCard.height
    faceDownCard.resize(100, 100*aspectRatio)
    imageH = height//2-(height*.32)
    for i in range(5):
        image(faceDownCard, (width//2+(width*.25)) -(2*i), imageH)
        
def giveCard(player):
    global deck, temporaryDraw, faceDownCard
    card = deck.pop()
    player.cards.append(card)
    if player is dealer:
        if len(player.cards) > 1:
            mvCard = MovingCard(card.img, PVector(width//2+(width*.25),height//2-(height*.32)), PVector(player.handPosition[0]-(len(player.cards)-2)*(card.img.width+20),player.handPosition[1]), card.makeVisible)
        else:
            if faceDownCard is None:
                faceDownCard = loadImage('green_back.png')
                aspectRatio = faceDownCard.width/faceDownCard.height
                faceDownCard.resize(100, 100*aspectRatio)
            mvCard = MovingCard(faceDownCard, PVector(width//2+(width*.25),height//2-(height*.32)), PVector(player.handPosition[0]-(len(player.cards)-2)*(card.img.width+20),player.handPosition[1]), card.makeVisible)
    else:
        mvCard = MovingCard(card.img, PVector(width//2+(width*.25),height//2-(height*.32)), PVector(player.handPosition[0]+(len(player.cards)-1)*(card.img.width+20),player.handPosition[1]), card.makeVisible) 
    temporaryDraw.append({'draw': mvCard, 'time': int(frameRate*1)})
    

def drawingFunction():
    global player, dealer, backgroundImage, temporaryDraw, counter
    if counter == 0:
        load()
        counter = 10
    else:
        counter -= 1
    background(backgroundImage)
    drawIntroScreen()
    if currentPlayer is not None or temporaryDraw:
        drawDeck()
        player.display()
        dealer.display()
    for i in range(len(temporaryDraw) - 1,-1,-1):
        obj = temporaryDraw[i]
        obj['time'] -= 1
        obj['draw']()
        if not obj['time']:
            temporaryDraw.pop(i)
        
def draw():
    drawingFunction()
        
add_library('net')
myClient = None
        
def load():
    global myClients, players, dealer, deck, currentPlayer
    myClients.append(Client(this, "localhost", 5000))
    myClients[-1].write("GET / HTTP/1.1\r\n")
    myClients[-1].write("\r\n")
    if(myClients[0].available() > 0):
        dataIn = myClients[0].readString()
        if('[]' not in dataIn):
            try:
                value = dataIn[dataIn.index('[') + 1:-1]
                if currentPlayer is not None:
                    player = players[currentPlayer]
                    if int(value) == 2:
                        currentPlayer += 1
                        if currentPlayer == len(players):
                            currentPlayer = None
                        else:
                            player = players[currentPlayer]
                    if int(value) == 1:
                        player.cards.append(deck.pop())
                        if player.isBust() or player.handValue() == 21:
                            if player.isBust():
                                temporaryDraw.append({'draw': drawBust, 'time': int(2*frameRate)})
                            currentPlayer += 1
                            if currentPlayer == len(players):
                                currentPlayer = None
            except:
                pass
        myClients.pop(0)
    while myClients and not myClients[0].active():
        myClients.pop(0)
