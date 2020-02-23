class Player(object):
    def __init__(self, handPosition, money):
        self.handPosition = handPosition
        self.money = money
        self.cards = None
        
    def display(self):
        displayX, displayY = self.handPosition
        if self.cards is not None:
            spacing = self.cards[0].img.width + 20
            for i in range(len(self.cards)):
                card = self.cards[i]
                card.display(displayX + i*spacing, displayY)
                
