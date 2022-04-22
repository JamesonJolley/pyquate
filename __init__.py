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


class point:
    def __init__(self,x = 0, y = 0):
        self.x = x
        self.y = y

    def git_x(self):
        return self.x

    def set_x(self, x = 0):
        self.x = x

    def git_y(self):
        return self.y

    def set_y(self,y = 0):
        self.y = y
        
        
        
#Areas
class Areas(compute):
    def __init__(self):
        super().__init__()
        self.area = compute_area()
        self.width = 0
        self.height = 0
        self.base = 0
        self.oragin = 0

    def compute_area():
        """
        Contains the formula and computes the area of the shape
        """
        return 0 
    
    def git_area(self):
        return self.area
    
    def git_width(self):
        return self.width

    def git_height(self):
        return self.height

    def git_base(self):
        return self.base

    def set_area(self,area = compute_area()):
        self.area = area

    def set_width(self,width=0):
        self.width = width

    def set_height(self,height=0):
        self.height = height

    
class Rectangle(Areas):
    def __init__(self,width=0,height=0):
        super().__init__()
        self.width = width
        self.height = height

    def compute_area(self):
        """
        Contains the formula and computes the area of the shape
        """
        Area = self.width * self.height
        return Area
    

class Triangle(Areas):
    def __init__(self,base=0,height=0):
        super().__init__()
        self.base = base
        self.height = height

    def compute_area(self):
        """
        Contains the formula and computes the area of the shape
        """
        Area = (self.base * self.height) / 2
        return Area

class Rhombus(Areas):
    def __init__(self,large_diagonal=0,small_diagonal=0):
        super().__init__()
        self.large_diagonal = large_diagonal
        self.small_diagonal = small_diagonal

    def compute_area(self):
        """
        Contains the formula and computes the area of the shape: Rhombus A = (D*d)/2
        """
        Area = (self.large_diagonal * self.small_diagonal) / 2
        return Area

    def git_large_diagonal(self):
        return self.large_diagonal

    def git_small_diagonal(self):
        return self.small_diagonal

    def set_large_diagonal(self,large_diagonal=0):
        self.large_diagonal = large_diagonal

    def set_small_diagonal(self,small_diagonal=0):
        self.small_diagonal = small_diagonal
 
class Trapezoid(Areas):
    def __init__(self,large_side=0,small_side=0,height=0):
        super().__init__()
        self.large_side = large_side
        self.small_side = small_side
        self.height = height

    def compute_area(self):
        """
        Contains the formula and computes the area of the shape: Trapezoid A = (B+b)/2*h
        """
        Area = (self.large_side + self.small_side) / 2 * self.height
        return Area

class Regular_polygon(Areas):
    def __init__(self,perimeter=0,apothem=0):
        super().__init__()
        self.perimeter = perimeter
        self.apothem = apothem
        
    def compute_area(self):
        """
        Contains the formula and computes the area of the shape: Trapezoid A = (B+b)/2*h
        """
        Area = self.perimeter / 2 * self.apothem
        return Area

    def git_perimeter(self):
        return self.perimeter

    def git_apothem(self):
        return self.apothem

    def set_perimeter(self,perimeter=0):
        self.perimeter = perimeter

    def set_apothem(self,apothem=0):
        self.apothem = apothem

        