from PIL import Image
imageName = "cover.gif"
Dir = "C:/includes/"
myImage = Dir + imageName
newImage = Dir + "Magnified-" + imageName

#Load and Create the image
with Image.open(myImage) as im:
    px = im.convert('RGB')
    px = px.load()
with Image.new("RGB", im.size, color=0) as newim:
    newpx = newim.load()
    
#Copy the Image
for i in range(im.height):
    for t in range(im.width):
        r = px[t,i][0]
        g = px[t,i][1]
        b = px[t,i][2]
        newpx[t,i] = (r,g,b)
        
#NOTE: I was unable to figure out a solution using the pixel method.
#       So I figured out the function method instead.
#Resize magnifies or shrinks the image to the specified Width and Height
#Then cropping it using the size contraints of the inital image will provide
#a "Zoomed in" result
newim = newim.resize((im.width*4,im.height*4))
newim = newim.crop((0,0,im.width,im.height))
newim.save(newImage)
im.show()
newim.show()