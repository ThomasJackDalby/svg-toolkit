from tools import *

line(0, 0, 100, 0)
line(100, 0, 100, 100)
line(100, 100, 0, 100)
line(0, 100, 0, 0)

stroke(255, 0, 0)
line(40, 40, 60, 60)
rect(10, 10, 90, 90)

stroke(0, 255, 0)
rect(20, 10, 10, 50)

stroke(0, 0, 0)
stroke_weight(4)

ellipse(50, 50, 10)
ellipse(20, 50, 10, 20)

save("test.svg")