"""
MAIN IDEA --> Initial Starting Point = (x,y)
Robot will move dx in x direction i.e x + dx
Robot will move dy in y direction i.e y + dy
Intially dx = 0 and dy = 1 because robot is pointing upward towards north

From Origin (0,0):  
N-->(0,1)
S-->(0,-1)
E-->(1,0)
W-->(-1,0)
If we encounter instruction 'L', and the current direction is North, robot will move towards West, If current direction is
East and we get a 'L', robot will start moving towards 'N'. Everytime we encounter 'L' or 'R', then update dx and dy depending upon
how the current direction will change if we move L or R.
Example if Current direction is west and we are asked to move R then robot will start moving towards N (North) !
"""

def isRobotBounded(instructions):
    """
    :type instructions: str
    :rtype: bool
    """
    x,y = 0,0               # Initial Starting Point
    dx = 0                  # Initial Change in x which is set because robot initally pointing northwards
    dy = 1
    direction = 'N'         # Intial direction
    for instruction in instructions:
        if instruction == 'G':          # Move forward in the current direction
            x = x + dx
            y = y + dy
        if instruction == 'L':          # If we get an instruction to move left
            if direction == 'N':        # Check if current direction is North
                dx = -1
                dy = 0
                direction = 'W'
            elif direction == 'E':
                dx = 0
                dy = 1
                direction = 'N'
            elif direction == 'S':      # Check if current direction is South
                dx = 1                  # Everytime think about current direction, and think in what next direction will robot start moving depending upon what we have encountered, L or R
                dy = 0
                direction = 'E'         # if current direction is North and we encounter a 'L', robot will start moving towards 'E' i.e east
            else:
                dx = 0
                dy = -1
                direction = 'S'
        if instruction == 'R':          # If we are asked to mvoe right
            if direction == 'N':
                dx = 1
                dy = 0
                direction = 'E'
            elif direction == 'E':      # Check for current direction everytime
                dx = 0                  
                dy = -1
                direction = 'S'
            elif direction == 'S':
                dx = -1
                dy = 0
                direction = 'W'
            else:
                dx = 0
                dy = 1
                direction = 'N'
    if (x == 0 and y == 0) or direction != 'N':
        return True
    else:
        return False

s = 'GLGLGGLGL'

print(isRobotBounded(s))