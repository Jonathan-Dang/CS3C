from PIL import Image
THRESHHOLD = 30 # color distance threshhold for determining if pixel should be black or white
BLACK = (0, 0, 0) # black pixel
WHITE = (255, 255, 255) # white pixel
imageName = "queen-mary.gif"
Dir = "C:/includes/"
myImage = Dir + imageName
newImage = Dir + "Traced-" + imageName

with Image.open(myImage) as im:
    px = im.convert('RGB')
    px = px.load()
with Image.new("RGB", im.size, color=0) as newim:
    newpx = newim.load()
#initialize all cardinal RGB values to 0
rE , rS , rSE , rN , rW , rNW , rSW , rNE = 0,0,0,0,0,0,0,0
gE , gS , gSE , gN , gW , gNW , gSW , gNE = 0,0,0,0,0,0,0,0
bE , bS , bSE , bN , bW , bNW , bSW , bNE = 0,0,0,0,0,0,0,0
for x in range(im.width):
    for y in range(im.height):
      
        # Current Pixel
        r = px[x,y][0]
        g = px[x,y][1]
        b = px[x,y][2]

        # Obtain Cardinal Direction's Pixels
        #East
        if (x != im.width - 1):
          rE = px[x + 1,y][0]
          gE = px[x + 1,y][1]
          bE = px[x + 1,y][2]
        #South
        if (y != im.height - 1):
          rS = px[x,y + 1][0]
          gS = px[x,y + 1][1]
          bS = px[x,y + 1][2]
        #South East
        if (x != im.width - 1 and y != im.height - 1):
          rSE = px[x + 1,y + 1][0]
          gSE = px[x + 1,y + 1][1]
          bSE = px[x + 1,y + 1][2]
        #West
        if (x != 0):
          rW = px[x - 1,y][0]
          gW = px[x - 1,y][1]
          bW = px[x - 1,y][2]
        #North
        if (y != 0):
          rN = px[x,y - 1][0]
          gN = px[x,y - 1][1]
          bN = px[x,y - 1][2]
        #North West
        if (x != 0 and y != 0):
          rNW = px[x - 1,y - 1][0]
          gNW = px[x - 1,y - 1][1]
          bNW = px[x - 1,y - 1][2]
        #North East
        if (x != im.width - 1 and y != 0):
          rNE = px[x + 1,y - 1][0]
          gNE = px[x + 1,y - 1][1]
          bNE = px[x + 1,y - 1][2]
        #South West
        if (x != 0 and y != im.height -1):
          rSW = px[x - 1,y + 1][0]
          gSW = px[x - 1,y + 1][1]
          bSW = px[x - 1,y + 1][2]

        # Now calculate average pixel
        rA = (rE + rS + rSE + rN + rW + rNW + rSW + rNE) / 8
        gA = (gE + gS + gSE + gN + gW + gNW + gSW + gNE) / 8
        bA = (bE + bS + bSE + bN + bW + bNW + bSW + bNE) / 8

        #Calculate the Distance
        distance = (r - rA) + (g - gA) + (b - bA)

        #Determine whether or not it should be either black or white.
        if distance > THRESHHOLD:
          newpx[x, y] = BLACK
        else:
          newpx[x,y] = WHITE

newim.save(newImage,'JPEG')
im.show()
newim.show()