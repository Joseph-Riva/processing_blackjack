

class MovingCard:
    
    def __init__(self, img, startPos, endPos, final):
        self.img = img
        self.startPos = startPos
        self.endPos = endPos
        self.numIterations = int(frameRate*1)
        self.curPos = self.startPos
        self.vec = endPos-startPos
        self.final = final
        self.iteration = 0
        
    def __call__(self):
        self.curPos += self.vec / self.numIterations
        self.iteration += 1
        image(self.img, self.curPos.x, self.curPos.y)    
        if self.iteration == self.numIterations:
            for cb in self.final:
                cb()
            
        
