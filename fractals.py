import turtle
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
import math
import tkinter 
from typing import List


@dataclass
class IsoscelesAngles:
    base_angle: float
    top_angle: float

@dataclass
class Points:
    X: List[int] 
    Y: List[int] 

# property of Isoceles Triangles
# (1) 2 * base_angle + top_angle = 180
# (2) => base_angle = (180 - top_angle) / 2
# (3) => top_angle = 180 - 2 * base_angle
# (4) => 180 - (top_angle + base_angle) = 180 - top_angle + base_angle = base_angle (look at 1)

# Save points for matplotlib
points = Points([], [])


def get_side_distance(base_distance, scaling_factor, num_triangles):
    return scaling_factor * base_distance / (2 * num_triangles)

def get_isosceles_angles(base_distance, side_distance):
    x = base_distance / (2 * side_distance)
    return IsoscelesAngles(base_angle= math.degrees(np.arccos(x)), top_angle= math.degrees(2 * np.arcsin(x))) 

def main_pattern(side_distance: float, angles: IsoscelesAngles, left: bool = True, repeat: int = 2) -> None:

    # get initial movements
    first_turn = turtle.left if left else turtle.right
    second_turn = turtle.right if left else turtle.left

    first_turn(angle = angles.base_angle)
    turtle.forward(side_distance)
    x, y = turtle.position()
    points.X.append(x)
    points.Y.append(y)
    for _ in range(repeat - 1):

        second_turn(angle = 180 - angles.top_angle)
        turtle.forward(side_distance)
        x, y = turtle.position()
        points.X.append(x)
        points.Y.append(y)

        first_turn(angle = 180 - angles.top_angle)
        turtle.forward(side_distance)
        x, y = turtle.position()
        points.X.append(x)
        points.Y.append(y)

    second_turn(angle= 180 - angles.top_angle)
    turtle.forward(side_distance)
    x, y = turtle.position()
    points.X.append(x)
    points.Y.append(y)

def recursive(n, side_distance, angles: IsoscelesAngles, left: bool = True):

    # start with main pattern
    # repeat smaller version of main pattern, n number of times 
    
    # get initial movements
    first_turn = turtle.left if left else turtle.right
    second_turn = turtle.right if left else turtle.left

    # first dimension
    main_pattern(side_distance=side_distance, angles= angles, left = left, repeat=n)
    first_turn(angle = 180)

    # second dimension
    side_distance = get_side_distance(side_distance, SCALING_FACTOR, num_triangles=num_triangles)
    for _ in range(n):
        main_pattern(side_distance= side_distance, angles= angles, left = left ^ True, repeat= n)
        # first_turn(angle= 180 - (angles.base_angle + angles.top_angle))
        first_turn(angle = angles.base_angle)  # same as 180 - (angles.base_angle + angles.top_angle)
        main_pattern(side_distance= side_distance, angles= angles, left = left ^ True, repeat= n)
        second_turn(angle = 180 - (angles.top_angle - angles.base_angle) )

    # third dimension
    # # to do another dimension remove last turn and restart the loop with a smaller scalling factor
    first_turn(angle = 180 - (angles.top_angle - angles.base_angle))
    first_turn(angle=180)
    side_distance = get_side_distance(side_distance, SCALING_FACTOR, num_triangles=num_triangles)
    
    for _ in range(n):
        # way up
        for _ in range(n):
            main_pattern(side_distance= side_distance, angles= angles, left = left, repeat= n)
            second_turn(angle = angles.base_angle)
            main_pattern(side_distance= side_distance, angles= angles, left = left, repeat= n)
            first_turn(angle = 180 - (angles.top_angle - angles.base_angle) ) 

        # at the top adjustment
        first_turn(angle = - (180 - (angles.top_angle - angles.base_angle)))
        first_turn(angle=angles.base_angle)
        
        # way down
        for _ in range(n):
            main_pattern(side_distance= side_distance, angles= angles, left = left, repeat= n)
            second_turn(angle = angles.base_angle)
            main_pattern(side_distance= side_distance, angles= angles, left = left, repeat= n)
            first_turn(angle = 180 - (angles.top_angle - angles.base_angle) ) 
        
        # at the bottom adjustment
        first_turn(angle = -(180 - (angles.top_angle - angles.base_angle) ) )
        first_turn(angle=180)
        first_turn(angle=angles.base_angle)
        first_turn(angle=angles.base_angle)
        second_turn(angle = angles.top_angle)
        first_turn(angle=angles.base_angle)
        # first_turn(angle=-angles.base_angle)
        

        # worked for scaling of 2
        # first_turn(angle = - (180 - (angles.top_angle - angles.base_angle) ) )
        # first_turn(angle= angles.base_angle)
        # first_turn(angle= 180)
        # first_turn(angle= angles.base_angle)

        # for _ in range(n):
        #     main_pattern(side_distance= side_distance, angles= angles, left = left, repeat= n)
        #     second_turn(angle = angles.base_angle)
        #     main_pattern(side_distance= side_distance, angles= angles, left = left, repeat= n)
        #     first_turn(angle = 180 - (angles.top_angle - angles.base_angle) ) 

        # first_turn(angle = - (180 - (angles.top_angle - angles.base_angle)))
        # first_turn(angle=angles.base_angle)
        
        # for _ in range(n):
        #     main_pattern(side_distance= side_distance, angles= angles, left = left, repeat= n)
        #     second_turn(angle = angles.base_angle)
        #     main_pattern(side_distance= side_distance, angles= angles, left = left, repeat= n)
        #     first_turn(angle = 180 - (angles.top_angle - angles.base_angle) ) 
    # first_turn(angle = 180 - (angles.top_angle - angles.base_angle))
    # first_turn(angle=180)

    # main_pattern(side_distance= get_side_distance(side_distance, SCALING_FACTOR, num_triangles= num_triangles), angles= angles, left = False, repeat= n)
    # turtle.left(angle = angles.base_angle)
    # main_pattern(side_distance= get_side_distance(side_distance, SCALING_FACTOR, num_triangles= num_triangles), angles= angles, left = False, repeat= n)

# Initial conditions
# turtle.left(angle=180)  # start by going on the right
num_triangles = 2  # tells me how much I should scale the ruler down by to see an increase in distance by SCALING_FACTOR
base_distance = 200
SCALING_FACTOR = 1.3
side_distance = get_side_distance(base_distance=base_distance, scaling_factor=SCALING_FACTOR, num_triangles=num_triangles)
angles = get_isosceles_angles(base_distance=(base_distance / num_triangles), side_distance=side_distance)
# turtle.radians()
# turtle.penup()
# turtle.setx(-350.0)
# turtle.sety(0.0)
# turtle.pendown()

print(f"turtle direction: {turtle.heading()}")
print(f"turtle position: {turtle.position()}")
print(f"first angle: {math.degrees(angles.base_angle)}")
print(f"side distance: {side_distance}")

turtle.speed(0)
x, y = turtle.position()
points.X.append(x)
points.Y.append(y)
recursive(num_triangles, side_distance=side_distance, angles=angles, left=True)

plt.plot(points.X, points.Y)
plt.show()
# must be placed at the end
# turtle.mainloop()


### Doing this with coordinate

# Positional vector: point and distance?
#                    two points
# two points will be easier to use with matplotlib

# Define two functions
# 1 - get points based on positional vector
# 2 - scale points down (needed?)
# 3 - recursion 