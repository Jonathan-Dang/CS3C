#Author: Jonathan Dang
#Assignment: Assignment 5 - Chapter 6
#Academic Honesty Pledge:
#   This assignment was created and written with my own work (Or additionally with the help of this week's partner)
#   and I(we) promise that we held academic integrity at all times during this assignment.
#   If I(we) have been inclined to create something based of off another's work, I(we) will include 
#   specific details pertaining to the assignment within the .py file of each project.
#   I(we) did not seek outside assistance that would violate academic integrity at any point in time, before and to the future
#   of this class.
#   -Jonathan Dang
from PIL import Image


##
#   shrinkImage:
#       Input: An opened Image object from PIL
#       Function: Shrinks the image by a factor of 2
#       Output: A modified image that is smaller than the original
def shrinkImage(openedImage):
    with openedImage as im:
        px = im.convert('RGB')
        px = px.load()
    with Image.new("RGB", (im.height//2,im.width//2), color=0) as newim:
        newpx = newim.load()
        
    for i in range(im.height//2):
            for t in range(im.width//2):
                r = px[t*2,i*2][0]
                g = px[t*2,i*2][1]
                b = px[t*2,i*2][2]
                newpx[t,i] = (r,g,b)
    return newim
    

##
#   addBorder:
#       Input: An opened Image object from PIL
#       Function: Adds a border to the picture
#       Output: A modified image that has a colored border
def addBorder(openedImage):
    ur = int(input("Please input the color value for the Red section: "))
    ug = int(input("Please input the color value for the Green section: "))
    ub = int(input("Please input the color value for the Blue section: "))
    borderWidth = int(input("Please input the width of the border in pixels: "))
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
            newpx[t,i] = (r,g,b)
    
    for wid in range(borderWidth):
        for i in range(im.height):
            newpx[wid,i] = (ur,ug,ub)
            newpx[im.width - 1 - wid,i] = (ur,ug,ub)
        for t in range(im.width):
            newpx[t,wid] = (ur,ug,ub)
            newpx[t,im.height - 1 - wid] = (ur,ug,ub)
    return newim
        


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
