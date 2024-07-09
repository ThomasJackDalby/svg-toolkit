from svg_toolkit import *
import math
import random
from spatial import Vector2D

class Cog:

    def __init__(self, x, y, number_of_teeth, tooth_width) -> None:
        self.x = x
        self.y = y
        self.number_of_teeth = number_of_teeth
        self.teeth_depth = radius * 0.1
        self.radius = radius
        self.inner_radius = self.radius - self.teeth_depth
        self.teeth_angle = 2 * math.pi / self.number_of_teeth

    def to_svg(self):
        d = f"M {self.x} {self.y} m {self.radius} 0 "
        for i in range(self.number_of_teeth):
            start_angle = i * self.teeth_angle
            mid_angle = (i + 0.5) * self.teeth_angle
            end_angle = (i + 1) * self.teeth_angle

            start_pos = Vector2D(self.radius * math.cos(start_angle), self.radius * math.sin(start_angle))
            mid_upper_pos = Vector2D(self.radius * math.cos(mid_angle), self.radius * math.sin(mid_angle))
            mid_lower_pos = Vector2D(self.inner_radius * math.cos(mid_angle), self.inner_radius * math.sin(mid_angle))
            end_lower = Vector2D(self.inner_radius * math.cos(end_angle), self.inner_radius * math.sin(end_angle))
            end_upper = Vector2D(self.radius * math.cos(end_angle), self.radius * math.sin(end_angle))

            a = mid_upper_pos - start_pos
            b = mid_lower_pos - mid_upper_pos
            c = end_lower - mid_lower_pos
            e = end_upper - end_lower

            d += f"a {self.radius} {self.radius} 0 0 1 {a.x} {a.y} "
            d += f"l {b.x} {b.y} "
            d += f"a {self.inner_radius} {self.inner_radius} 0 0 1 {c.x} {c.y} "
            d += f"l {e.x} {e.y} "

        # d += f"M {self.x + 40} {self.y} "
        # d += f"a 40 40 0 0 0 -80 0 "
        # d += f"a 40 40 0 0 0 80 0 "

        path = dominate.svg.path(
            stroke="black",
            fill="white",
            stroke_width="2",
            d = d
        )
        g += path
        return g

if __name__ == "__main__":

    width = 200
    height = 200

    for i in range(10):    
        x = random.random() * width
        y = random.random() * height
        radius = random.random() * 50 + 10
        teeth = random.choice(range(5, 30))
        cog = Cog(x, y, radius, teeth)
        cog.draw()

    save("cogs.svg")