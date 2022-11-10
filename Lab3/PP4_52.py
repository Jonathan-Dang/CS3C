from PIL import Image
imageName = "queen-mary.gif"
Dir = "C:/includes/"
myImage = Dir + imageName
newImage = Dir + "GreyScaled-" + imageName

#Load and Create
with Image.open(myImage) as im:
    px = im.convert('RGB')
    px = px.load()
with Image.new("RGB", im.size, color=0) as newim:
    newpx = newim.load()
    
for i in range(im.height):
    for t in range(im.width):
        r = px[t,i][0]
        g = px[t,i][1]
        b = px[t,i][2]
        #This is the Grey Ratio, I didn't use the ratios as stated in the book
        #as it was too red to be considered GreyScale
        grey = (r + g + b) // 3
        #Make sure its a TUPLE and not a single integer as not doing so
        #maxes the values of the other color sections.
        #(grey) => (grey, 255 ,255)
        newpx[t,i] = (grey,grey,grey)
        
newim.save(newImage,'JPEG')
im.show()
newim.show()
