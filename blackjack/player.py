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
    
    def handValue(self):
        total = 0
        aces = 0
        for card in self.cards:
            val = min(10, card.value)
            if val == 1:
                aces += 1
                total += 11
            else:
                total += val
        if total > 21:
            while aces > 0 and total > 21:
                aces -= 1
                total -= 10
        return total
        
    def display(self):
        displayX, displayY = self.handPosition
        if self.cards is not None:
            spacing = self.cards[0].img.width + 20
            for i in range(len(self.cards)):
                card = self.cards[i]
                card.display(displayX + i*spacing, displayY)
        handTotal = self.handValue()
        fill(0, 0, 0)
        if len(self.cards) == 2 and handTotal == 21:
            text("Blackjack!", displayX, displayY - 25)
        elif handTotal > 21:
            fill(255, 40, 40)
            text("Bust!", displayX, displayY - 25)
        else:
            text("Hand total: " + str(self.handValue()), displayX, displayY - 25)
            
                
