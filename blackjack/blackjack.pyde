def setup():
    size(1080, 720)
    textSize(60)

letter = ''

def keyPressed():
    global letter
    if type(key) == type(u'a') and ord(key) < 256:
        if ord(key) == 8:
            letter = letter[:-1]
        else:
            letter += key
            print(key, letter)
    
def draw():
    global letter
    frameRate(12)
    background(0)
    text(letter, mouseX, mouseY)
