"""
This Module implements the Ship class, as well as associated Parts for the "BareBones"
of Battleship.
"""


import string

#CONSTANTS
DIRECTION_TRANSLATOR = {'N':1 , 'E':2, 'S':3, "W":4}
DIRECTIONS = ['N','E','S','W']
EMPTY_SPACE_INDICATOR = "\0"
SHIP_TYPES = {1:"Carrier", 2:"Battleship", 3:"Cruiser", 4:"Submarine", 5:"Destroyer"}
SHIP_SIZES = {1:5, 2:4, 3:3, 4:3, 5:2}
ALPHABET = string.ascii_uppercase


class Point():
    """
    Object to store two integers in coordinate style. Restrictive version of a Tuple
    """
    def __init__(self, x: int = -1, y: int = -1) -> None:
        """

        Args:
            x (int, optional): Position of Coordinate's X variable. Defaults to -1.
            y (int, optional): Position of Coordinate's Y variable. Defaults to -1.
        """
        self.x = x
        self.y = y  
    
    def __repr__(self) -> str:
        """

        Returns:
            _type_: Representation of the coordinate
        """
        return f"({self.x},{self.y})"
    
    def __str__(self) -> str:
        """ 
        Returns a string version of the object

        Returns:
            str: String version of the object
        """
        return f"({self.x},{self.y})"
    
    def __eq__(self,rhs) -> bool:
        """
        Sub-method that checks if the two objects are the same
            
        Args:
            rhs (_type_): object being compaired to

        Returns:
            bool: True: if the object instance is the same and if the x and y variables are equal
        """
        return rhs.x == self.x and rhs.y == self.y

class Ship():
    """
    Ship object that is the interactable object of the Battleship! game.
    """
    def __init__(self, type: int = -1) -> None:
        if type in SHIP_TYPES:
            self._name = SHIP_TYPES[type]
            self._size = SHIP_SIZES[type]
        else:
            #ValueError is basically Parameter Error, having name convertion to numbers for better
            #management.
            raise ValueError("Type must be from range of 1 to 5 only.")
        #Index is the link between position and hit position
        self._position = [Point()] * self._size
        self._hits = [False] * self._size
        self._orientation = ""
        self.Sunk = False
        
    def _checkSunk(self) -> bool:
        """
        Checks if the ship is sunk, if so then mark the ship as Sunk.
        
        Returns:
            bool: True if the ship has all it's positions Hit
        """
        #Restricts the method for re-visit processing time
        if self.Sunk is True:
            return self.Sunk
        
        for part in self._hits:
            if not part:
                return False
        self.Sunk = True
        return True
        
    def setPosition(self,x:int, y:int, orientation:str) -> None:
        """
        Sets the position of the ship
        
        Args:
            x (int): X position of the head of the ship
            y (int): Y position of the head of the ship
            orientation (str): The orientation for the rest of the ship

        Raises:
            ValueError:99: Checks the orientation for a valid direction for proper placement.\n
            ValueError:116: Unforseen error catch.
        """
        if orientation not in DIRECTIONS:
            raise ValueError("Invalid Orientation, Please use N,E,S, or W as The Orientation")
        
        self._orientation = orientation
        
        if DIRECTION_TRANSLATOR[orientation] == 4: #WEST
            for i in range(self._size):
                self._position[i] = Point(x - i,y)
        elif DIRECTION_TRANSLATOR[orientation] == 3: #SOUTH
            for i in range(self._size):
                self._position[i] = Point(x,y + i)
        elif DIRECTION_TRANSLATOR[orientation] == 2: #EAST
            for i in range(self._size):
                self._position[i] = Point(x + i,y)
        elif DIRECTION_TRANSLATOR[orientation] == 1: #NORTH
            for i in range(self._size):
                self._position[i] = Point(x,y - i)
        else:
            #This line is not needed, however it is safer to have it as it is possible for magic error
            raise ValueError("Direction resulted in None type or not designated value")
        
class ShipMispositionError(ValueError):
    """
    Error that signifies a miss-position of a ship. As such, extends ValueError
    
    Args:
        ValueError (_type_): Super Class
    """
    def __init__(self, *args: object) -> None:
        """
        Initializes an error
        """
        super().__init__(*args)

class gameBoard():
    """
    Gameboard is the main interacting system of Battleship!
    """
    def __init__(self, side_length: int = 10) -> None:
        """
        Inializing the gameboard

        Args:
            side_length (int, optional): The length of this gameboard. Defaults to 10.
        """
        self._board = []
        for i in range(10):
            temp = []
            for t in range(10):
                temp.append(EMPTY_SPACE_INDICATOR)
            self._board.append(temp)
        self._side = side_length
        self._ships = []
        
    #NOTE:MEANT ONLY FOR DEBUGGING
    def __repr__(self) -> str:
        ret = "■ 1 2 3 4 5 6 7 8 9 10\n-+-+-+-+-+-+-+-+-+-+-\n"
        for row in range(self._side):
            ret += ALPHABET[row] + '|'
            for col in range(self._side):
                if self._board[row][col] is not EMPTY_SPACE_INDICATOR:
                    ret += self._board[row][col]
                else:
                    ret += " "
                if col != self._side - 1:
                    ret += '|'
            if row != self._side - 1:
                ret += '\n'
                ret += "-+"*(self._side) + '-'
                ret += '\n'
        return ret
    
    def Done(self) -> bool:
        """
        Checks if all ships are hit and Sunk

        Returns:
            bool: True if all ships are hit and sunk
        """
        ship : Ship
        for ship in self._ships:
            for hit in ship._hits:
                if not hit:
                    return False
        return True
    
    def FIRE(self, x: int, y : int) -> bool:
        """
        Fires at a location x,y | X and Y are in Coordinate Form.

        Args:
            x (int): X coordinate of the shot taken
            y (int): Y coordinate of the shot taken

        Returns:
            bool: True if the the shot hit.
        """
        if self.isPositionShip(x,y):
            ships = self._ships
            ship : Ship
            for ship in ships:
                for pos in ship._position:
                    if pos.x is x and pos.y is y:
                        ship._hits[ship._position.index(Point(x,y))] = True
                        ship._checkSunk()
                        return True
        else:
            return False
    
    def isPositionShip(self, x : int, y : int) -> bool:
        """
        Checks if the position X,Y is a ship| X and Y are in Coordinate Form

        Args:
            x (int): X coordinate of the shot taken
            y (int): Y coordinate of the shot taken

        Returns:
            bool: True if the position is a Ship
        """
        return self._board[y][x] is not EMPTY_SPACE_INDICATOR
    
    def getShipPositions(self) -> list[list]:
        """
        Obtains all the ship's positions in list form.

        Returns:
            list[list]: Returns a list with all the lists of the ship's positions
        """
        ret = []
        ship : Ship
        for ship in self._ships:
            ret.append(ship._position)
        
        return ret
    
    def placeShip(self, x : int, y : int, ship : Ship, orientation : str) -> bool:
        """
        Adds a ship to the game board. MAX OF 5

        Args:
            x (int): X coordinate of the head of the ship
            y (int): Y coordinate of the head of the ship
            ship (Ship): A ship to be placed.
            orientation (str): Direction of the placement of the ship.

        Raises:
            ValueError:265: Invalid Positional Input\n
            ValueError:270: Invalid Orientation\n
            ValueError:273: Maximum Ships Placed\n
            ShipMispositionError:271:284:297:310: Ship Doesn't Fit into position specified\n
            ShipMispositionError:275:288:301:214: Ship already present at the location

        Returns:
            bool: True if successfully placed
        """
        if x > self._side or x < 0 or y > self._side or y < 0:
            raise ValueError(f"Invalid X or Y position: x:{x}, y:{y}")
        
        orientation = orientation.upper()
        
        if orientation not in DIRECTIONS:
            raise ValueError(f"Invalid orientation input")
        
        if len(self._ships) > 5:
            raise ValueError("Maximum Ship count reached")
        
        if DIRECTION_TRANSLATOR[orientation] == 4:#WEST
            if (x - ship._size) < 0:
                raise ShipMispositionError("Ship does not fit into position with said orientation!")
            else:
                for i in range(ship._size):
                    if self.isPositionShip(x - i,y):
                        raise ShipMispositionError("Ship already present at this location")
                
                ship.setPosition(x,y,orientation)
                self._ships.append(ship)
                for coord in ship._position:
                    self._board[coord.y][coord.x] = "S"
            return True
        elif DIRECTION_TRANSLATOR[orientation] == 3:#SOUTH
            if (y + ship._size) >= self._side:
                raise ShipMispositionError("Ship does not fit into position with said orientation!")
            else:
                for i in range(ship._size):
                    if self.isPositionShip(x,y + i):
                        raise ShipMispositionError("Ship already present at this location")
                
                ship.setPosition(x,y,orientation)
                self._ships.append(ship)
                for coord in ship._position:
                    self._board[coord.y][coord.x] = "S"
            return True
        elif DIRECTION_TRANSLATOR[orientation] == 2:#EAST
            if (x + ship._size) >= self._side:
                raise ShipMispositionError("Ship does not fit into position with said orientation!")
            else:
                for i in range(ship._size):
                    if self.isPositionShip(x + i,y):
                        raise ShipMispositionError("Ship already present at this location")
                
                ship.setPosition(x,y,orientation)
                self._ships.append(ship)
                for coord in ship._position:
                    self._board[coord.y][coord.x] = "S"
            return True
        elif DIRECTION_TRANSLATOR[orientation] == 1:#NORTH
            if (y - ship._size) < 0:
                raise ShipMispositionError("Ship does not fit into position with said orientation!")
            else:
                for i in range(ship._size):
                    if self.isPositionShip(x,y - i):
                        raise ShipMispositionError("Ship already present at this location")
                
                ship.setPosition(x,y,orientation)
                self._ships.append(ship)
                for coord in ship._position:
                    self._board[coord.y][coord.x] = "S"
            return True
        return False