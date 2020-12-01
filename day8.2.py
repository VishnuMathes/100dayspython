# calculate the number of paint cans to paint a wall
import math

def paint_calc(height, width, cover ):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You'll need {round_up_cans} to paint the wall")

test_h = int(input("Height of the wall:"))
test_w = int(input("Width of the wall:"))
coverage = 5


paint_calc(height= test_h, width = test_w, cover = coverage)





