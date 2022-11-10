import random
from types import NoneType
import pygame
import json

from Ship import *

#CONSTANTS
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
BOARD_SIDE = (WINDOW_WIDTH // 2) - 200
TILE_WIDTH = BOARD_SIDE // 10 #Divisions
HOVER_COLOR = (255,255,0)
PLACED_COLOR = (194,197,204)
HIT_COLOR = (255,0,0)
WATER_COLOR = (0,125,225)
MISSED_COLOR = (0,0,0)

class PlayerBoardBackground(pygame.sprite.Sprite):
    """
    A Sprite object that holds the background of the grid for Battleship!

    Args:
        pygame (Sprite): Base Sprite Class
    """
    def __init__(self, xOffset:int = 0,leftJustified:bool = True):
        """
        Initializes the object

        Args:
            xOffset (int, optional): Offset from the border of the screen. Defaults to 0.
            leftJustified (bool, optional): Determines if the object is left justified. Defaults to True.
        """
        pygame.sprite.Sprite.__init__(self)
        
        #Background
        self.image = pygame.Surface([BOARD_SIDE,BOARD_SIDE])
        self.image.fill(WATER_COLOR)
        self.rect = self.image.get_rect()
        self._offset = xOffset
        if leftJustified:
            self.rect.topleft = ((WINDOW_WIDTH - (BOARD_SIDE * 2))//3 + xOffset,((WINDOW_WIDTH - (BOARD_SIDE * 2))//3))
        else:
            self.rect.topright = (WINDOW_WIDTH - (WINDOW_WIDTH - (BOARD_SIDE * 2))//3,((WINDOW_WIDTH - (BOARD_SIDE * 2))//3))
            
    def getTilePositions(self) -> list:
        """
        Obtains the tile positions of this object in relation of a certain size and returns them.

        Returns:
            list: 2D list of all the positions of each grid in pixel coordinate form.
        """
        grid = []
        for i in range(10):
            row = []
            for spacer in range(self.rect.left,self.rect.right,TILE_WIDTH):
                x = spacer
                y = self.rect.top + (TILE_WIDTH * i)
                row.append(Point(x,y))
            grid.append(row)
        return grid         #TopLeft position
    
class ShipSprite(pygame.sprite.Sprite):
    """
    A Sprite object that holds the Ship for Battleship!

    Args:
        pygame (Sprite): Base Object for this class
    """
    def __init__(self, ship : Ship, orientation : string, board : PlayerBoardBackground, opponent : bool = False) -> None:
        """
        Initializes this object

        Args:
            ship (Ship): Ship object passed by Assignment {Meant for outside linking}
            orientation (string): Orientation of the Ship
            board (PlayerBoardBackground): Visual Aspect of the Game Board
            opponent (bool, optional): Determines if this ship is the opponent's. Defaults to False.
        """
        pygame.sprite.Sprite.__init__(self)
        self._ship = ship
        #Restricted Placement method. Helps with rectangle generation and positioning
        if orientation == 'N' or orientation == 'S':
            self.image = pygame.Surface((TILE_WIDTH,TILE_WIDTH*ship._size + 1))
        else:
            self.image = pygame.Surface((TILE_WIDTH * ship._size + 1,TILE_WIDTH))
            
        #Flag that controls visibility
        if opponent:
            self.image.fill(WATER_COLOR)
        else:
            self.image.fill(PLACED_COLOR)
            
        #Automatically sets the position to ontop of the board object
        self.rect = self.image.get_rect()
        self.rect.topleft = board.rect.topleft
        self.rect.left += ship._position[0].x * TILE_WIDTH
        self.rect.top += ship._position[0].y * TILE_WIDTH
        
    #Overwrite Sprite.update()
    def update(self):
        """
        Updates the ship object based on hit status
        """
        #NOTE: The position of the draw.rect is in constant reference to the display, first parameter and WILL NOT leak out of the display.
        for hit in range(self._ship._size):
            if self._ship._hits[hit]:
                if self._ship._orientation == 'S':
                    pygame.draw.rect(self.image,HIT_COLOR,pygame.Rect(0, hit * TILE_WIDTH,TILE_WIDTH,TILE_WIDTH))
                elif self._ship._orientation == 'E':
                    pygame.draw.rect(self.image,HIT_COLOR,pygame.Rect(hit*TILE_WIDTH, 0,TILE_WIDTH,TILE_WIDTH))
                    
class MissedShipSprite(pygame.sprite.Sprite):
    """
    Filler Sprite to show a missed Shot

    Args:
        pygame (Sprite): Base Class for the object
    """
    #Just a filler sprite.
    def __init__(self, rect : pygame.Rect) -> None:
        """
        Initializes the object using a rectangle

        Args:
            rect (pygame.Rect): A preset and placed rectangle on the board.
        """
        super().__init__()
        self.image = pygame.Surface((TILE_WIDTH,TILE_WIDTH))
        self.rect = rect
        self.image.fill(MISSED_COLOR)
            
def drawGrid(screen : pygame.display, boardSprite: PlayerBoardBackground):
    """
    Draws the grid Lattice overlay ontop of a board sprite

    Args:
        screen (pygame.display): The display of the entire game
        boardSprite (PlayerBoardBackground): The board recieving the overlay
    """
    blockSize = TILE_WIDTH #Set the size of the grid block
    for x in range(boardSprite.rect.x, BOARD_SIDE + boardSprite.rect.x, blockSize):
        for y in range(boardSprite.rect.y, BOARD_SIDE + boardSprite.rect.y, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            #The last parameter changes the color from fill to border
            pygame.draw.rect(screen, (0,0,0), rect, 1)
            
def Convert_Reference_to_Direction(point: tuple[int,int], x: int, y: int) -> str:
    """
    Generates a direction based on a reference point and an additional coordinate location

    Args:
        point (tuple[int,int]): The Reference Point
        x (int): X of the addtional position
        y (int): Y of the addtional position

    Returns:
        String : A singular Capitalized character that indications a direction
    """
    #Think about the diagonals as they might be considered as both directions they are diagonal to.
    
    if abs((point[0] - x)) == abs((point[1] - y)):
        return None
    
    #take the point of reference and another point, subtract to each other to have the dx and dy.
    dx = abs(point[0] - x)
    dy = abs(point[1] - y)
    
    if dx > dy:
        if point[0] - x > 0:
            return 'N'
        else:
            return 'S'
    else:
        if point[1] - y > 0:
            return 'W'
        else:
            return 'E'
        
class BattleShipGame():
    """
    The brain and heart of the Battleship Game
    """
    def __init__(self):
        """
        Loads the game and initializes itself to default values.
        """
        pygame.init()
        self._display = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption("Battleship!")
        self._clock = pygame.time.Clock()
        self._framesPerSecond = 30
        self._BackgroundSprites = pygame.sprite.LayeredUpdates()
        self._foregroundSprites = pygame.sprite.LayeredUpdates()
        self._ticks = 0
        self._display.fill((255,255,255))
        pygame.key.set_repeat(1, 120)
        
        
        try:
            playerBoard = gameBoard()
            self._loadPlayerData(playerBoard)
        except Exception as ex:
            print(ex)
            exit(1)
        
        player = PlayerBoardBackground()
        opponentBoard = PlayerBoardBackground(leftJustified= False)
        opponent = self._loadRandomOpponent()
        ship : Ship
        for ship in playerBoard._ships:
            self._foregroundSprites.add(ShipSprite(ship,ship._orientation,player))
        for ship in opponent._ships:
            self._foregroundSprites.add(ShipSprite(ship,ship._orientation,opponentBoard,opponent=True))
        self._BackgroundSprites.add(player, opponentBoard) 
        self._system = [playerBoard, opponent]  #pass by assignment -> Reference {C++} 
        self._tilePositions = self._obtainTileCoords()  #List[list(Point), list(Point)]
        self._tiles = self._createTileRectangles() #Now: List[list(Rect),list(Rect)]
        
        self._opponentShots = []
        self._opponentShotStatus = []
        self._opponentAdvicedMoves = []
        self._playerShots = []
    
    def update(self):
        """
        Calls all sprite's update method
        """
        self._BackgroundSprites.update()
        self._foregroundSprites.update()
        
    def run(self):
        """
        Runs the game
        """
        Turn = True
        active = True
        while True:
            mouseCoords = pygame.mouse.get_pos()
            
            for sprite in self._BackgroundSprites:
                if isinstance(sprite,PlayerBoardBackground):
                    drawGrid(boardSprite = sprite,screen= self._display)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit() 
                    return;
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.__init__()
                
                if event.type == pygame.MOUSEBUTTONDOWN and active:
                    pos = self._tileCoordinateConversion(mouseCoords[0],mouseCoords[1])
                    if Turn and not isinstance(pos,NoneType) and pos[1] == 1:
                        if self._playerShots.count(Point(pos[0][0],pos[0][1])) == 0:
                            if self._system[1].FIRE(pos[0][0],pos[0][1]):
                                #print("HIT!")
                                PLACEHOLDER = 0
                            else:
                                rect = self._getTileatPosition(mouseCoords[0],mouseCoords[1])
                                self._foregroundSprites.add(MissedShipSprite(rect))
                            #saves the shot to have no repeat shots.
                            self._playerShots.append(Point(pos[0][0],pos[0][1]))
                            Turn = False

            if not Turn:
                self._enemyReturnFire()
                Turn = True
                        
            if self._system[0].Done() or self._system[1].Done():
                if self._system[1].Done():
                   self._PlayerWin()
                else:
                   self._OpponentWin()
                #Disables the game after the win status
                active = False
                
            self._hoveredTile(mouseCoords[0],mouseCoords[1])
            pygame.display.update()
            self._display.fill((255,255,255))
            self.draw()
            self.update()
                 
    def draw(self) :
        """
        Calls the draw method on all sprites
        """
        self._BackgroundSprites.draw(self._display)
        self._foregroundSprites.draw(self._display)
        
    def _PlayerWin(self):
        """
        Declares the player a winner!
        """
        font = pygame.font.Font("freesansbold.ttf",60)
        text = font.render("You Win! Press \"r\" to reset the game", True, (0,255,0),(0,0,0))
        textRect = text.get_rect()
        textRect.center = self._display.get_rect().center
        self._display.blit(text, textRect)
        #print("Player Win!")
    
    def _OpponentWin(self):
        """
        Declares the opponent a winner!
        """
        font = pygame.font.Font("freesansbold.ttf",60)
        text = font.render("You Lose! Press \"r\" to reset the game", True, (255,0,0),(0,0,0))
        textRect = text.get_rect()
        textRect.center = self._display.get_rect().center
        self._display.blit(text, textRect)
        #print("Opponent Win!")
        
    def _enemyReturnFire(self):
        """
        The opponent fires against the player.
        """
        if len(self._opponentAdvicedMoves) > 0:
            #Prioritizes all shots advized
            pos = self._opponentAdvicedMoves.pop()
            hit = self._system[0].FIRE(pos.x,pos.y)
            if not hit:
                self._foregroundSprites.add(MissedShipSprite(self._tiles[0][pos.y][pos.x]))
            self._opponentShotStatus.append(hit)
            self._opponentShots.append(pos)
        else:
            #Repeats until a valid shot is taken
            while True:
                x = random.randint(0,9)
                y = random.randint(0,9)
                pos = Point(x,y)
                if self._opponentShots.count(pos) == 0:
                    hit = self._system[0].FIRE(x,y)
                    if not hit:
                        self._foregroundSprites.add(MissedShipSprite(self._tiles[0][y][x]))
                    self._opponentShotStatus.append(hit)
                    self._opponentShots.append(pos)
                    break;
        self._updateAILocationed()
            
    def _updateAILocationed(self):
        """
        Updates the Adviced locations depending on all shots taken
        """
        for it in range(len(self._opponentShotStatus) - 1,0,-1):
            if self._opponentShotStatus[it]:
                pos = self._opponentShots[it]
                x = pos.x
                y = pos.y
                if x + 1 <= 9 and self._opponentShots.count(Point(x + 1,y)) == 0 and self._opponentAdvicedMoves.count(Point(x + 1,y)) == 0:
                    self._opponentAdvicedMoves.append(Point(x + 1,y))
                if x - 1 >= 0 and self._opponentShots.count(Point(x - 1,y)) == 0 and self._opponentAdvicedMoves.count(Point(x - 1,y)) == 0:
                    self._opponentAdvicedMoves.append(Point(x - 1,y))
                if y + 1 <= 9 and self._opponentShots.count(Point(x,y + 1)) == 0 and self._opponentAdvicedMoves.count(Point(x,y + 1)) == 0:
                    self._opponentAdvicedMoves.append(Point(x,y + 1))
                if y - 1 >= 0 and self._opponentShots.count(Point(x,y - 1)) == 0 and self._opponentAdvicedMoves.count(Point(x,y - 1)) == 0:
                    self._opponentAdvicedMoves.append(Point(x,y - 1))
        
    def _loadPlayerData(self, board :gameBoard):
        """
        Loads the player's ship positions.

        Args:
            board (gameBoard): The player's board state
        """
        filename = "PlayerBoardState.JSON"
        try:
            ins = open(filename,'r')
            data = json.loads(ins.read())
            i = 1
            for ship in data["Ships"]:
                board.placeShip(ship["x"],ship["y"],Ship(i),ship["Orientation"])
                i += 1
        except Exception as e:
            print(e)
            exit(1)
        finally:
            ins.close()
            
    def _loadRandomOpponent(self) -> gameBoard:
        """
        Randomly generates the opponent's board

        Returns:
            gameBoard: The opponent's board
        """
        board = gameBoard()
        for i in range(1,6):
            try:
                board.placeShip(random.randint(0,9),random.randint(0,9),Ship(i),random.choice(['S','E']))
            except ShipMispositionError as e:
                while True:
                    try:
                        if board.placeShip(random.randint(0,9),random.randint(0,9),Ship(i),random.choice(['S','E'])):
                            break;
                    except ShipMispositionError as e:
                        #Keep on trying any possible space until a valid one comes up
                        continue
                continue
        return board
        
    def _obtainTileCoords(self) -> list:
        """
        Obtains and saves all tile coordinates for both grids

        Returns:
            list: A list that contains two lists that hold all tile coordinates.
        """
        ret = []
        grid : PlayerBoardBackground
        for grid in self._BackgroundSprites.sprites():
            ret.append(grid.getTilePositions())
        return ret
    
    def _createTileRectangles(self) ->list[list]:
        """
        From the internal positions, makes pygame.Rect for each one.

        Returns:
            list[list]: Translated Rectangle List
        """
        ret = []
        for grid in self._tilePositions:
            grid_set = []
            for row in grid:
                layer = []
                for pos in row:
                    layer.append(pygame.rect.Rect(pos.x,pos.y,TILE_WIDTH,TILE_WIDTH))
                grid_set.append(layer)
            ret.append(grid_set)
        return ret

    def _hoveredTile(self, x: int, y: int) -> None:
        """
        Draws a reticale for the hovered tile.

        Args:
            x (int): X variable for the hovered tile | In Pixel Coordinate Form
            y (int): Y variable for the hovered tile | In Pixel Coordinate Form
        """
        tile = self._getTileatPosition(x,y)
        if tile:
            pygame.draw.rect(self._display,(255,155,0),tile, TILE_WIDTH//10, TILE_WIDTH)
            
    def _tileCoordinateConversion(self, x: int, y: int) -> tuple[tuple[int,int],int] | None:
        """
        Converts the Pixel Coordinate to a coordinate plane form, as well as determine which
        board is being selected

        Args:
            x (int): X position of the mouse coordinate
            y (int): X position of the mouse coordinate

        Returns:
            tuple[tuple[int,int],int] | None: Returns the Tuple if the position is a valid tile
        """
        grid: list
        row: list
        gridpos = 0
        for grid in self._tiles:
            for row in range(10):
                for col in range(10):
                    #Using Collide Point to allow for specific location of the rectangle
                    if grid[row][col].collidepoint(x,y):
                        return ((col,row), gridpos);
            gridpos += 1
        
        return None
    
    #x and y is mouse coords
    def _getTileatPosition(self, x: int, y: int) -> pygame.rect.Rect | None:
        """
        Returns a Rectangle based on mouse position

        Args:
            x (int): X position of the mouse coordinate
            y (int): X position of the mouse coordinate

        Returns:
            pygame.rect.Rect | None: Returns the hovered Rectangle, None if no rectangle hovered
        """
        grid: list
        row: list
        rect : pygame.rect.Rect
        for grid in self._tiles:
            for row in grid:
                for rect in row:
                    if rect.collidepoint(x,y):
                        return rect;    
                    
        return None

    def quit(self) -> None:
        """
        Quits the game
        """
        pygame.quit()
            
    #Deprecated - Used only to debug _obtainTileCoords for hover Mechanics and Processings pre-requisits
    """def _DEBUG_SubRectanglPositions(self):
        ins = open("TEST-POSITION-SUBRECTANGLE.txt",'w')
        grids = self._BackgroundSprites.sprites()
        for grid in grids:
            for row in grid.getTilePositions():
                for point in row:
                    ins.write(str(point))
                ins.write('\n')
            ins.write('\n\n\n')
        ins.close()"""
           
           
def main():
    game = BattleShipGame()
    game.run()

main()