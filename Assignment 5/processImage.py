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
from imageProcessingFunctions import *

##
#   Main:
#           Input: An image file
#           Primary Function: Provides a menu to edit a singular image in the provided ways, then displays the modified image
#           Output: A modified image
def main():
    #Input and Read Section=============================================================================================
    filename = input("Enter the name of the image file to be processed [Be Sure to include the filehandle]: ")
    if filename.count('.') == 0:
        filehandle = input("Please input the filehandle:")
    else: 
        filehandle = filename[len(filename)-4:len(filename)]
    dir = input("Please enter the directory of the image file [DEFAULT: \"C:/includes/\"]:")
    if len(dir) == 0:
        dir = "C:/includes/"

    #Pre-Processing=====================================================================================================
    newImage = Image.open(dir + filename)
    while True :
        # Prompt the user for the type of processing.
        print("How should the image be processed?")
        print("1 - create image negative")
        print("2 - adjust brightness")
        print("3 - flip vertically")
        print("4 - rotate to the left")
        print("5 - shrink the image")
        print("6 - add a border")
        print("7 - save and quit")

        response = int(input("Enter your choice: "))
        #Processing the image per response==============================================================================
        #Reversing all the color pixels
        if (response == 1):
            newImage = createNegative(newImage)
        #Adjust the brightness of the entire image
        elif (response == 2):
            newImage = adjustBrightness(newImage)
        #Flipping the image along the x-axis that is placed directly at the image's center
        elif (response == 3):
            newImage = flipVertically(newImage)
        #Rotating the image 90 degrees Clockwise
        elif (response == 4):
            newImage = rotateLeft(newImage)
        elif (response == 5):
            newImage = shrinkImage(newImage)
        elif (response == 6):
            newImage = addBorder(newImage)
        #Saving and exiting=============================================================================================
        elif (response == 7):
            newImage.save(filename.replace('.',"-Modified."))
            break;
    newImage.show()
            
main()
        