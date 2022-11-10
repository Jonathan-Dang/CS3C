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
        print("X - save and quit")

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
        #Saving and exiting=============================================================================================
        elif (response == int('X') or response == int('x')):
            savedFileHandle = input("Please enter your desired filehandle to save the image as [Leave blank if you want the original handle]:")
            if len(savedFileHandle) == 0:
                newImage.save(filename)
            else:
                newImage.save(filename,savedFileHandle)
            break;
    newImage.show()
            
main()
        