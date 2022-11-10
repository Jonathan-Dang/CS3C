from PIL import Image
imageName = "cover.gif"
Dir = "C:/includes/"
myImage = Dir + imageName
newImage = Dir + "Multiplied-" + imageName

#Load and Create Section
with Image.open(myImage) as im:
    px = im.convert('RGB')
    px = px.load()
with Image.new("RGB", im.size, color=0) as newim:
    newpx = newim.load()
    
#Without Functions
for i in range(im.height):
    for t in range(im.width):
        if (i % 2 == 0 and t % 2 == 0):
            r = px[t,i][0]
            g = px[t,i][1]
            b = px[t,i][2]
            #This is "Cropping" and "Shrinking"
            #by taking every even pixel, we can essentially shrink the image by a factor of 4.
            #Then this series of commands is positioning the image at the 4 essential positions
            #Along the x and y axis, and then directly in the center.
            newpx[t//2 ,i//2] = (r,g,b)
            newpx[(t//2) + im.width//2 ,i//2] = (r,g,b)
            newpx[(t//2) + im.width//2 ,i//2 + im.height//2] = (r,g,b)
            newpx[t//2 ,i//2 + im.height//2] = (r,g,b)
#Save as a JPEG
newim.save(newImage,'JPEG')
im.show()
newim.show()

#With Functions
'''with Image.open(myImage) as im:
    resizedIm = im.resize((im.width // 2, im.height // 2))
with Image.new("RGB", im.size, color=0) as newim:
    newim.paste(resizedIm,(0,0))
    newim.paste(resizedIm,(0,im.height//2))
    newim.paste(resizedIm,(im.width//2,0))
    newim.paste(resizedIm,(im.width//2,im.height//2))
        
newim.save(newImage,'JPEG')
im.show()
newim.show()'''