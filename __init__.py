import math

# base inherated classes
class compute:
    """
    The base class for all computations in this Library. Users will not interact with this class directly.
    """
    def __init__(self):
        self.solution = self.equation()
        pass

    def equation(self):
        """
        Contains the formula and computes the solution
        """
        return None
    
    def get_solution(self):
        return self.solution

#Areas

class Rectangle(compute):
    def __init__(self,width=0,height=0):
        super().__init__()
        self.width = width
        self.height = height

    def equation(self):
        """
        Contains the formula and computes the solution
        """
        Area = self.width * self.height
        return Area
    

class Triangle(compute):
    def __init__(self,base=0,height=0):
        super().__init__()
        self.base = base
        self.height = height

    def equation(self):
        """
        Contains the formula and computes the solution
        """
        Area = (self.base * self.height) / 2
        return Area


