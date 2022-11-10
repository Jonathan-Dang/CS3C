from PIL import Image
imageName = "queen-mary.gif"
Dir = "C:/includes/"
myImage = Dir + imageName
newImage = Dir + "Rotated-" + imageName

with Image.open(myImage) as im:
    px = im.convert('RGB')
    px = px.load()
#Image size is a Tuple of size 2, swapping the height and width will set the image 90 degrees
with Image.new("RGB", [im.height,im.width] , color=0) as newim: #This is now 90 degrees converted either way
    newpx = newim.load()
    
    
#px[Width,Height]
transposedI = im.height - 1
for i in range(im.height):
    for t in range(im.width):
        r = px[t,i][0]
        g = px[t,i][1]
        b = px[t,i][2]
        #We must go backwards in terms of width, so it would be rotated and not rotated flipped
        newpx[transposedI,t] = (r,g,b)
    transposedI -= 1
        
#Save as a JPEG
newim.save(newImage,'JPEG')
im.show()
newim.show()