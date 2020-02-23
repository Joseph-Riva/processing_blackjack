img = createImage(2000, 2000, RGB)
img.loadPixels()
for i in range(len(img.pixels)): 
    if (noise(i, random(1)) > .70):
        for j in range(i-3, i):
            img.pixels[i] = color(100*noise(i), 100*noise(i), 100*(noise(i)))
    else:
        img.pixels[i] = color(8, 124, 95)
img.updatePixels()
#image(img,0,0)
#save("table.png")
def setup():
    size(1000,1000)
    background(0)

def draw():
    image(img, 0, 0)
    save("table.png")
    exit()
