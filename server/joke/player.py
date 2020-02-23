from cards import faceToValue
fontsize = 20

class Player(object):
    def __init__(self, handPosition, money):
        self.handPosition = handPosition
        self.money = money
        self.cards = None
        self.playing = True
        
    def isBust(self):
        value = 0
        for card in self.cards:
            value += min(10, card.value)
            if value > 21:
                return True
        return False
        
    def display(self):
        displayX, displayY = self.handPosition
        if self.cards is not None:
            spacing = self.cards[0].img.width + 20
            for i in range(len(self.cards)):
                card = self.cards[i]
                card.display(displayX + i*spacing, displayY)
        if self.isBust():
            fill(255, 40, 40)
            text("Bust!", displayX, displayY - 25)
            
                
