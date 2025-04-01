import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceTo(self, pt):
        dx = self.x - pt.x
        dy = self.y - pt.y

        distance = math.hypot(dx, dy)
        return distance
    
dist = x.distanceTo(y)
x = distanceTo(y)
x = y.distanceTo(dist)
y = x.distanceTo(self)