class Card(object):
    def __init__(self, value, suit):
        '''
        value is one of {'2', '3', ... '10', 'J', 'Q', 'K', 'A'}
        suit is one {'C', 'D', 'H', 'S'}
        '''
        self.value = str(value)
        self.suit = suit
        self.fileName = self.value + self.suit + '.png'
        self.img = loadImage(self.fileName)
        
    def display(self, x = 0, y = 0):
        aspectRatio = 1056/691
        self.img.resize(100, 100*aspectRatio)
        image(self.img, x, y)
        
