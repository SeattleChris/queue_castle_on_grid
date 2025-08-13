#!/bin/python3

import os
from collections import namedtuple, deque

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

OPEN = '.'
BLOCK = 'X'

def minimumMoves(grid, startX, startY, goalX, goalY):
    """For grid, X represents the row and Y is for the column."""
    height = len(grid)  # for x
    width = len(grid[0])  # for y
    Node = namedtuple('Node', ['x', 'y', 'steps'])
    visited = [[False] * width for _ in range(height)]
    moves = deque()
    moves.append(Node(startX, startY, 0))
    visited[startX][startY] = True

    while moves:
        curr = moves.popleft()
        if (curr.x, curr.y) == (goalX, goalY):
            return curr.steps
        cx, cy = curr.x, curr.y
        while cx > 0 and grid[cx - 1][cy] != BLOCK:
            cx -= 1
        while cx < height and grid[cx][cy] != BLOCK:
            if not visited[cx][cy]:
                moves.append(Node(cx, cy, curr.steps + 1))
                visited[cx][cy] = True
            cx += 1
        cx = curr.x  # cy was unchanged
        while cy > 0 and grid[cx][cy - 1] != BLOCK:
            cy -= 1
        while cy < width and grid[cx][cy] != BLOCK:
            if not visited[cx][cy]:
                moves.append(Node(cx, cy, curr.steps + 1))
                visited[cx][cy] = True
            cy += 1
    return -1  # Should never reach this point if given valid inputs.


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    first_multiple_input = input().rstrip().split()
    startX = int(first_multiple_input[0])
    startY = int(first_multiple_input[1])
    goalX = int(first_multiple_input[2])
    goalY = int(first_multiple_input[3])
    result = minimumMoves(grid, startX, startY, goalX, goalY)
    fptr.write(str(result) + '\n')
    fptr.close()
