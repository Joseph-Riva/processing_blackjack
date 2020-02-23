from cards import Card
from player import Player

faceDownCard = None

class Dealer(Player):
    
    def __init__(self, handPosition):
        global faceDownCard
        if not faceDownCard:
            faceDownCard = loadImage('green_back.png')
            aspectRatio = faceDownCard.width/faceDownCard.height
            faceDownCard.resize(100, 100*aspectRatio)
        self.handPosition = handPosition
        self.cards = []
        self.cardRevealed = False
        self.playing = True
    
        
    def display(self):
        global faceDownCard
        displayX, displayY = self.handPosition
        if self.cards:
            spacing = self.cards[0].img.width + 20
            startIdx = 1
            if len(self.cards) > 0 and not self.cardRevealed:
                image(faceDownCard, displayX + spacing, displayY)
            elif len(self.cards) > 0:
                startIdx = 0
                fill(0, 0, 0)
                text(self.getHandStatus(), displayX, displayY + 27 + faceDownCard.height)
            for i in range(startIdx, len(self.cards)):
                card = self.cards[i]
                card.display(displayX - (i-1)*spacing, displayY)
