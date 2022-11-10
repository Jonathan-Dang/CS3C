from PIL import Image
imageName = "queen-mary.gif"
Dir = "C:/includes/"
myImage = Dir + imageName
newImage = Dir + "RedTinted-queen-mary.jpg"

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
        #This scaling is given from the book
        newpx[t,i] = (round(r * 1.3),round(g*.667),round(b*.667))
        
#Documentation from the PIL website states that when changing file types, its safer to place the type when saving
newim.save(newImage,'JPEG')
im.show()
newim.show()