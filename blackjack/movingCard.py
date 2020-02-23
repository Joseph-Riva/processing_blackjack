

class MovingCard:
    
    def __init__(self, img, startPos, endPos):
        self.img = img
        self.startPos = startPos
        self.endPos = endPos
        self.numIterations = int(frameRate*1)
        self.curPos = self.startPos
        self.vec = endPos-startPos
        
    def __call__(self):
        self.curPos += self.vec / self.numIterations
        image(self.img, self.curPos.x, self.curPos.y)    
            
        
