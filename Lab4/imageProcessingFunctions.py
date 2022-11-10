from PIL import Image

##
#   createNegative:
#       Input: An opened Image object from PIL
#       Function: Obtains every pixel and breaks it down to RGB values, then subtracts it from 255, 
#                   aka the max color value, then returns the modified image.
#       Output: A modified image that is "negative"
def createNegative(openedImage):
    with openedImage as im:
        px = im.convert('RGB')
        px = px.load()
    with Image.new("RGB", im.size, color=0) as newim:
        newpx = newim.load()
        
    for i in range(im.height):
        for t in range(im.width):
            r = px[t,i][0]
            g = px[t,i][1]
            b = px[t,i][2]
            r = 255 - r
            g = 255 - g
            b = 255 - b
            newpx[t,i] = (r,g,b)
    return newim

##
#   adjustBrightness:
#       Input: An opened Image object from PIL
#       Function: Obtains every pixel and breaks it down to RGB values, then multiplies it by a selected ratio, returning a modified image
#       Output: A modified image that is brighter or less bright than the original
def adjustBrightness(openedImage):
    brightness = int(input("Please input the new brightness level in percent, leaving out the sign itself [Do not input '%']: "))
    with openedImage as im:
        px = im.convert('RGB')
        px = px.load()
    with Image.new("RGB", im.size, color=0) as newim:
        newpx = newim.load()
        
    for i in range(im.height):
        for t in range(im.width):
            r = px[t,i][0]
            g = px[t,i][1]
            b = px[t,i][2]
            r = round(r * brightness)
            g = round(g * brightness)
            b = round(b * brightness)
            newpx[t,i] = (r,g,b)
            
    return newim

##
#   flipVertically:
#       Input: An opened Image object from PIL
#       Function: Flips the entire image upon the x-axis which is located at the center of the image by transposing
#                   each pixel.
#       Output: A modified image that is flipped vertically
def flipVertically(openedImage):
    with openedImage as im:
        px = im.convert('RGB')
        px = px.load()
    with Image.new("RGB", im.size, color=0) as newim:
        newpx = newim.load()
        
    for x in range(im.width):
        newy = im.height - 1
        for y in range(im.height):
            r = px[x,y][0]
            g = px[x,y][1]
            b = px[x,y][2]
            newpx[x,newy] = (r,g,b)
            newy -= 1
    return newim

##
#   rotateLeft:
#       Input: An opened Image object from PIL
#       Function: Creates a new image to hold a rotated left version of the original, then
#               transposes each pixel to accomidate for the change.
#       Output: A modified image that is rotated left
def rotateLeft(openedImage):
    with openedImage as im:
        px = im.convert('RGB')
        px = px.load()
    #Image size is a Tuple of size 2, swapping the height and width will set the image 90 degrees
    with Image.new("RGB", [im.height,im.width] , color=0) as newim: #This is now 90 degrees converted either way
        newpx = newim.load()
        
    transposedI = im.height - 1
    for i in range(im.height):
        for t in range(im.width):
            r = px[t,i][0]
            g = px[t,i][1]
            b = px[t,i][2]
            #We must go backwards in terms of width, so it would be rotated and not rotated flipped
            newpx[transposedI,t] = (r,g,b)
        transposedI -= 1
    return newim
