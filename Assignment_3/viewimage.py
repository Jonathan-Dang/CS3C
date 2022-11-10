#Note to peer reviewer: The Directory should be the file in which you place this file along with the jpg
#Please place the file directly in the C drive, along with this file and the flipimage.py
from PIL import Image
imageName = "Coggers.jpg"
Dir = "C:/"
myImage = Dir + imageName
im = Image.open(myImage)
im.show()