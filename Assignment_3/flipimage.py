#Note to peer reviewer: The Directory should be the file in which you place this file along with the jpg
#Please place the file directly in the C drive, along with this file and the viewfile.py
from PIL import Image
imageName = "Resident Sleeper.jpg"
newImageName = "FlippedSleeper.jpg"
Dir = "C:/includes/"
myImage = Dir + imageName
newImage = Dir + newImageName
with Image.open(myImage) as im:
    px = im.load()
with Image.new(im.mode, im.size, color=0) as newim:
    newpx = newim.load()

#newim = im.transpose(method = Image.FLIP_LEFT_RIGHT)
newi = im.height - 1
for i in range(im.height):
    for t in range(im.width):
        r = px[i,t][0]
        g = px[i,t][1]
        b = px[i,t][2]
        newpx[newi,t] = (r,g,b)
    newi -= 1

newim.save(newImage)
im.show()
newim.show()