##
#    Author: Jonathan Dang
#    Project: Toolbox 10 - 1 | Assignment 12
#    Date: 4/11/2022
#
'''
This assignment was created and written with my own work 
and I promise that I held academic integrity at all times during this assignment.
If I have been inclined to create something based of off another's work, I will include 
specific details pertaining to the assignment within the .py file of each project.
I did not seek outside assistance that would violate academic integrity at any point in time, before and to the future
of this class.
-Jonathan Dang
'''
from gamebase import GameBase, ImageSprite
import pygame
from random import randint
from os.path import exists as fileExists


def main():
   game = SnakeGame()
   game.run()


class Snake(ImageSprite):
    def __init__(self, x, y):
        super().__init__(x, y, "snake.bmp")
        self._alive = True
        self._layer = 2
        self._win = False


      ##
      #  keyDown(key):
      #     Input: Key
      #     Process: Checks if certain directional keys are pressed, updates position
      #     Output: None
      #
    def keyDown(self, key):
        if self._alive and not self._win:
            distance = 20
            if key == pygame.K_w or key == pygame.K_UP:
                self.moveBy(0, -distance)
            elif key == pygame.K_a or key == pygame.K_LEFT:
                self.moveBy(-distance, 0)
            elif key == pygame.K_s or key == pygame.K_DOWN:
                self.moveBy(0, distance)
            elif key == pygame.K_d or key == pygame.K_RIGHT:
                self.moveBy(distance, 0)

         ##
        #   die():
        #       Input: None
        #       Process: "Kills" the entity
        #       Output: None
        #
    def die(self):
        if self._alive:
            self.image = pygame.transform.flip(self.image, True, True)
            self._alive = False

         ##
        #   win():
        #       Input: None
        #       Process: Changes the _win variable to True
        #       Output: None
        #
    def win(self):
        self._win = True


class Car(ImageSprite):
    def __init__(self, x, lane):
        self._lane = lane
        y = 300 + 200 * lane
        super().__init__(x, y, "car" + str(randint(0, 9)) + ".bmp")

        if lane == 0:
            self.image = pygame.transform.flip(self.image, True, False)
        self._layer = 1

      ##
        #   update():
        #       Input: None
        #       Process: Updates the object to either auto-scroll left or right
        #
    def update(self):
        if self._lane == 0:
            self.rect.x += 1
        else:
            self.rect.x -= 1


class SnakeGame(GameBase):
   def __init__(self):
      super().__init__(1200, 600)
      self._snake = Snake(400, 600)
      self._frog = ImageSprite(400, 100, "frog.bmp")
      self._cars = pygame.sprite.Group()
      
      self._save = True;
      
      self._showScoreBoard = True
      
      self.SCOREBOARD_FILE = "scoreboard.txt"
      
      self._usernameInput = False
      self._instanceUsername = ""
      self._input_rect = pygame.Rect(0,0,140,32)

      if not fileExists(self.SCOREBOARD_FILE):
         open(self.SCOREBOARD_FILE, 'x')

   def getScores(self):
      # ORDER = ['RANK', 'NAME', 'SCORE']
      record = []
      try:
         ins = open(self.SCOREBOARD_FILE, 'r')
         for line in ins:
            dataLine = line.split(' ')
            record.append((dataLine[1], int(dataLine[2])))
      except Exception as e:
         print(e)
         exit(1)
      finally:
         ins.close()
         return record
      
   def saveScores(self, name : str):
      if not self._snake._alive or self._snake._win:
         record = self.getScores()
         score = 999999 - (100 * (self.getTicks() - 480))
         
         if not self._snake._alive:
            score -= 100000
         
         entry = (name, score)
         record.append(entry)
         record.sort(key = lambda x:x[1],reverse=True)
         
         with open(self.SCOREBOARD_FILE, 'w') as outs:
            for rank in range(len(record)):
               scoring = str(rank + 1) + ' ' + record[rank][0] + ' ' + str(record[rank][1]) + '\n'
               outs.write(scoring)
            outs.close()
      else:
         return;

   def addCar(self, lane):
      if lane == 0:
         x = - 100
      else:
         x = self._width - 400
      newCar = Car(x, lane)
      self._cars.add(newCar)
      self.add(newCar)

   def keyDown(self, key : pygame.event, event : pygame.event = None):
      self._snake.keyDown(key)
      if not self._usernameInput:
         if key == pygame.K_r:
            # main() also works, but results in stack overflow and memory leaks
            self.__init__()
      else:
         if key == pygame.K_BACKSPACE:
            self._instanceUsername = self._instanceUsername[:-1]
         elif key == pygame.K_RETURN:
            self._usernameInput = False
         else:
            if len(self._instanceUsername) < 3:
               self._instanceUsername += event.unicode

   def mouseButtonDown(self, x, y):
      if self._input_rect.collidepoint(x,y):
         self._usernameInput = True
      else:
         self._usernameInput = False
      return
   
   def saveOnce(self):
      if self._save:
         self.saveScores(self._instanceUsername)
         self._save = False

   def update(self):
      super().update()
      
      font = pygame.font.Font('freesansbold.ttf', 32)
      green = (0, 255, 0)
      blue = (0, 0, 128)
      
      pygame.draw.line(self._display,(0,0,0),(800,0),(800,self._height),5)
      pygame.draw.rect(self._display,(255,255,255),pygame.rect.Rect(800,0,400,self._height))
      
      record = self.getScores()
      displayStr = []
      rank = 1
      for entry in record:
         rankStr = str(rank) + entry[0] + ' ' + str(entry[1])
         rank += 1
         displayStr.append(rankStr)
         
      for index in range(len(displayStr)):
         text = font.render(displayStr[index], True, green, blue)
         textRect = text.get_rect()
         textRect.top = 35*index
         textRect.left = 800
         self._display.blit(text,textRect) 
      
      if self._usernameInput:
         text = font.render(self._instanceUsername, True, green, blue)
         textRect = text.get_rect()
         textRect.top = 0
         textRect.left = 0
         self._display.blit(text,textRect)
         self._clock.tick(self._framesPerSecond // 4)
      elif self._instanceUsername != "":
         text = font.render(self._instanceUsername, True, green, blue)
         textRect = text.get_rect()
         textRect.top = 0
         textRect.left = 0
         self._display.blit(text,textRect)  
      else:
         text = font.render("Insert 3 Letter Indicator Here", True, green, blue)
         textRect = text.get_rect()
         textRect.top = 0
         textRect.left = 0
         self._display.blit(text,textRect)

      if self.getTicks() % 240 == 0:  # Add a new car to each lane
         self.addCar(0)
         self.addCar(1)

      if self.getTicks() == 480:
         self.add(self._snake)
         self.add(self._frog)

      if pygame.sprite.spritecollideany(self._snake, self._cars):
         self._snake.die()
         self.saveOnce()

      if (pygame.sprite.collide_rect(self._snake, self._frog)):
         self._frog.kill()
         self._snake.win()
         self.add(ImageSprite(self._snake.rect.x, self._snake.rect.y, "crown.bmp"))
         self.saveOnce()

      if self._snake._win or not self._snake._alive:
         text = font.render("Press \"r\" to reset the game!", True, green, blue)
         textRect = text.get_rect()
         textRect.center = (400, 200)
         self._display.blit(text, textRect)


# Start the program.
main()
