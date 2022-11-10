import pygame

##
#  GameBase()
#     Purpose: Sets up a base game
#
class GameBase:
   def __init__(self, width, height):
      pygame.init()
      self._width = width
      self._height = height
 
      self._display = pygame.display.set_mode((self._width, self._height))
      self._clock = pygame.time.Clock()
      self._framesPerSecond = 30
      self._sprites = pygame.sprite.LayeredUpdates()
      self._ticks = 0
      pygame.key.set_repeat(1, 120) #comment
  
   ##
   #  mouseButtonDown(x,y):
   #     Input: The location of the mouse when the button down event occurs.
   #     Process: None
   #     Output: None
   #
   def mouseButtonDown(self, x, y):
      return
   
   ##
   #  keyDown(key)
   #     Input: A key press
   #     Process: None
   #     Output: None
   #
   def keyDown(self, key : pygame.event, event : pygame.event = None) :
      return
   
   ##
   #  update()
   #     Input: None
   #     Process: Updates all monitored sprites
   #     Output: None
   #
   def update(self) :
      self._sprites.update()
    
   ##
   #  draw()
   #     Input: None
   #     Process: Draws all monitored sprites
   #
   def draw(self) :
      self._sprites.draw(self._display)
    
   ##
   #  add(sprite)
   #     Input: A sprite
   #     Process: Adds a sprite to the game
   #     Output: None
   #
   def add(self, sprite) :
      self._sprites.add(sprite)
        
   ##
   #  getTicks()
   #     Input: None
   #     Process: None
   #     Output: Returns the internal tick rate
   #
   def getTicks(self):
      return self._ticks
        
   ##
   #  quit()
   #     Input: None
   #     Process: Quits the pygame internal system
   #     Output: None
   #
   def quit(self) :
      pygame.quit()      
   
   ##
   #  run()
   #     Input: None
   #     Process: Runs the base game 
   #     Output: None
   #
   def run(self):
      while True:
         for event in pygame.event.get() :
            if event.type == pygame.QUIT :
               self.quit()
               return;
            elif event.type == pygame.MOUSEBUTTONDOWN :                    
               self.mouseButtonDown(event.pos[0], event.pos[1])
            elif event.type == pygame.KEYDOWN :
               self.keyDown(event.key, event)
                    
         WHITE = (255, 255, 255)
         self._display.fill(WHITE)
         self.draw()
         self.update()
         pygame.display.update()
         self._clock.tick(self._framesPerSecond)
         self._ticks += 1
    
    
##
#  ImageSprite(pygame.sprite.Sprite)
#     An internal Sprite Object to be used with the gamebase object
#
class ImageSprite(
      pygame.sprite.Sprite):
   def __init__(self, x, y, filename) :
      super().__init__()
      self.loadImage(x, y, filename)
   
   ##
   #  loadImage(x,y,filename):
   #     Input: The position to spawn in the image as well as the image itself
   #     Process: Loads the image into the current game screen at location x,y
   #     Output: None
   #
   def loadImage(self, x, y, filename) :
      img = pygame.image.load(filename).convert()
      MAGENTA = (255, 0, 255)
      img.set_colorkey(MAGENTA)
      self.image = img
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y - self.rect.height
     
   ##
   #  moveBy(dx,dy):
   #     Input: The change in position
   #     Process: Moves the object by a certain amount dx,dy
   #     Output: None
   #
   def moveBy(self, dx, dy) :
      self.rect.x += dx
      self.rect.y += dy
 

