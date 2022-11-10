from PIL import Image
imageName = "queen-mary.gif"
Dir = "C:/includes/"
myImage = Dir + imageName
newImage = Dir + "Filtered-queen-mary.jpg"

#Section in which it loads / converts GIF to JPEG
with Image.open(myImage) as im:
    px = im.convert('RGB')
    px = px.load()
with Image.new("RGB", im.size, color=0) as newim:
    newpx = newim.load()
    
#Read and Write
for i in range(im.height):
    for t in range(im.width):
        r = px[t,i][0]
        g = px[t,i][1]
        b = px[t,i][2]
        r = 255 - r
        g = 255 - g
        b = 255 - b
        newpx[t,i] = (r,g,b)
        
#Save as a JPEG
newim.save(newImage,'JPEG')
im.show()
newim.show()