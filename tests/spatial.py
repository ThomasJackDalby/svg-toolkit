import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def normalise(self):
        magnitude = self.abs()
        return Vector2D(self.x / magnitude, self.y / magnitude)

    def abs(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def to_tuple(self):
        return (self.x, self.y)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return (self.x * other.y) - (self.y * other.x)

    def get_perpendicular(self):
        return Vector2D(-self.y, self.x)

    def rotate(self, angle):
        s = math.sin(angle)
        c = math.cos(angle)
        return Vector2D(self.x * c - self.y * s, self.x * s + self.y * c)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2D(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector2D(self.x / other, self.y / other)

def is_zero(value):
    return abs(value) <= 1e-6

class Segment2D:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def to_tuple(self):
        return (self.start.to_tuple(), self.end.to_tuple())

    def intersect(self, other):
        p = self.start
        r = self.end - self.start
        q = other.start
        s = other.end - other.start
        
        rxs = r.cross(s)
        qmpxr = (q - p).cross(r)
        if is_zero(rxs):
            if is_zero(qmpxr): # collinear
                return None # fix
            else:
                return None # parallel and non-intersecting
        else: # not parallel
            qmpxs = (q - p).cross(s)
            u = qmpxr / rxs
            t = qmpxs / rxs
            if t > 0 and t < 1 and u > 0 and u < 1:
                return p + r * t
            else:
                # not parallel and do not intersect
                return None

    def intersects(self, other):
        p1 = self.start
        q1 = self.end
        p2 = other.start
        q2 = other.end
        
        # Find the 4 orientations required for
        # the general and special cases
        o1 = orientation(p1, q1, p2)
        o2 = orientation(p1, q1, q2)
        o3 = orientation(p2, q2, p1)
        o4 = orientation(p2, q2, q1)
    
        # General case
        if ((o1 != o2) and (o3 != o4)):
            return True
    
        # Special Cases
    
        # p1 , q1 and p2 are collinear and p2 lies on segment p1q1
        if ((o1 == 0) and onSegment(p1, p2, q1)):
            return True
    
        # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
        if ((o2 == 0) and onSegment(p1, q2, q1)):
            return True
    
        # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
        if ((o3 == 0) and onSegment(p2, p1, q2)):
            return True
    
        # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
        if ((o4 == 0) and onSegment(p2, q1, q2)):
            return True
    
        # If none of the cases
        return False
 
def onSegment(p, q, r):
    if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
           (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
        return True
    return False
 
def orientation(p, q, r):
    # to find the orientation of an ordered triplet (p,q,r)
    # function returns the following values:
    # 0 : Collinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise
     
    # See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/
    # for details of below formula.
     
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if (val > 0):
        # Clockwise orientation
        return 1
    elif (val < 0):
        # Counterclockwise orientation
        return 2
    else:
        # Collinear orientation
        return 0 