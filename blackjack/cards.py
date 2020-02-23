valToFace = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
faceToVal = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}

def valueToFace(cardVal):
    global valToFace
    if cardVal in valToFace:
        return valToFace[cardVal]
    return str(cardVal)

def faceToValue(cardFace):
    global faceToVal
    if cardFace in faceToVal:
        return faceToVal[cardFace]
    return int(cardFace) 

class Card(object):
    def __init__(self, value, suit):
        '''
        value is one of {'2', '3', ... '10', 'J', 'Q', 'K', 'A'}
        suit is one {'C', 'D', 'H', 'S'}
        '''
        self.face = str(value)
        self.value = faceToValue(self.face)
        self.suit = suit
        self.fileName = self.face + self.suit + '.png'
        self.img = loadImage(self.fileName)
        aspectRatio = self.img.width/self.img.height
        self.img.resize(100, 100*aspectRatio)
        self.visible = False
        
    def makeVisible(self):
        self.visible = True
        
    def display(self, x = 0, y = 0):
        if self.visible:
            image(self.img, x, y)
        
