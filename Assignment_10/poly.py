
class Value:
    def __init__(self, input):
        if not str(input).isalnum():
            validation = str(input)
            for char in "[+-*/!^()]":
                validation = validation.replace(char,'')
            if not validation.isalnum():
                raise ValueError("Invalid Input")
        
        self._value_ = input;
        
    def isNumber(self):
        return str(self._value_).isdigit()
    
    def isVariable(self):
        return str(self._value_).isalpha()
    
    def isExpression(self):
        validation = str(self._value_)
        for char in "[+-*/!^()]":
            validation = validation.replace(char,'')
        return validation.isalnum()
    
    def _SameType_(self, rhs):
        return isinstance(rhs,Value)
    
    def __add__(self, rhs):
        if self._SameType_(rhs):
            if (self.isVariable() or self.isExpression()) and (rhs.isVariable() or rhs.isExpression()):
                return Value(self._value_ + '+' + rhs._value_)
            else:
                return Value(self._value_ + rhs._value_)
        else:
            if isinstance(rhs,[int,float,complex]):
                return Value(self._value_ + rhs)
            elif isinstance(rhs,str):
                return Value(self._value_ + '+' + rhs)
            
    def __sub__(self, rhs):
        if self._SameType_(rhs):
            if (self.isVariable() or self.isExpression()) and (rhs.isVariable() or rhs.isExpression()):
                return Value(self._value_ + '-' + rhs._value_)
            else:
                return Value(self._value_ - rhs._value_)
        else:
            if isinstance(rhs,[int,float,complex]):
                return Value(self._value_ - rhs)
            elif isinstance(rhs,str):
                return Value(self._value_ + '-' + rhs)
            
    def __mul__(self, rhs):
        if self._SameType_(rhs):
            if (self.isVariable() or self.isExpression()) and (rhs.isVariable() or rhs.isExpression()):
                return Value(self._value_ + '*' + rhs._value_)
            else:
                return Value(self._value_ * rhs._value_)
        else:
            if isinstance(rhs,[int,float,complex]):
                return Value(self._value_ * rhs)
            elif isinstance(rhs,str):
                return Value(self._value_ + '*' + rhs)
        
    def __truediv__(self, rhs):
        if self._SameType_(rhs):
            if (self.isVariable() or self.isExpression()) and (rhs.isVariable() or rhs.isExpression()):
                return Value(self._value_ + '/' + rhs._value_)
            else:
                return Value(self._value_ / rhs._value_)
        else:
            if isinstance(rhs,[int,float,complex]):
                return Value(self._value_ / rhs)
            elif isinstance(rhs,str):
                return Value(self._value_ + '/' + rhs)
    
    def __pow__(self, rhs):
        if self._SameType_(rhs):
            if (self.isVariable() or self.isExpression()) and (rhs.isVariable() or rhs.isExpression()):
                return Value(self._value_ + '^(' + rhs._value_ + ')')
            else:
                return Value(self._value_ ** rhs._value_)
        else:
            if isinstance(rhs,[int,float,complex]):
                return Value(self._value_ ** rhs)
            elif isinstance(rhs,str):
                return Value(self._value_ + '^(' + rhs + ')')
    
    def __gt__(self, rhs):
        if not self._SameType_(rhs):
            if isinstance(rhs,[int,float,complex]):
                return self.isNumber() and self._value_ > rhs
            elif isinstance(rhs,str):
                return self.isNumber() and str.isdigit() and self._value_ > float(rhs)
            else:
                return False;
        else:
            return self._value_ > rhs._value_
    
    def __ge__(self, rhs):
        return self.__gt__(rhs) and self.__et__(rhs)
        
    def __lt__(self, rhs):
        if not self._SameType_(rhs):
            if isinstance(rhs,[int,float,complex]):
                return self.isNumber() and self._value_ < rhs
            elif isinstance(rhs,str):
                return self.isNumber() and str.isdigit() and self._value_ < float(rhs)
            else:
                return False;
        else:
            return self._value_ < rhs._value_
        
    def __le__(self, rhs):
        return self.__lt__(rhs) and self.__et__(rhs)
        
    def __et__(self, rhs):
        if not self._SameType_(rhs):
            if isinstance(rhs,[int,float,complex]):
                return self.isNumber() and self._value_ == rhs
            elif isinstance(rhs,str):
                return self.isNumber() and str.isdigit() and self._value_ == float(rhs)
            else:
                return False;
        else:
            return self._value_ == rhs._value_
    
    def __repr__(self):
        return self._value_