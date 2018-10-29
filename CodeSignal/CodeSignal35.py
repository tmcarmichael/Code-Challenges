def chessKnight(cell):
    x = ord(cell[0])-97
    y = int(cell[1])-1
    count = 0
    for i in range(1,3):
        for j in range(1,3):
            if i != j:
                if (x-i >= 0 and x-i < 8) and (y-j >= 0 and y-j < 8):
                    count += 1
                if (x-i >= 0 and x-i < 8) and (y+j >= 0 and y+j < 8):
                    count += 1
                if (x+i >= 0 and x+i < 8) and (y-j >= 0 and y-j < 8):
                    count += 1
                if (x+i >= 0 and x+i < 8) and (y+j >= 0 and y+j < 8):
                    count += 1
    return count


"""
Given a position of a knight on the standard chessboard, 
find the number of different moves the knight can perform.

The knight can move to a square that is two squares 
horizontally and one square vertically, or two squares 
vertically and one square horizontally away from it. The 
complete move therefore looks like the letter L. Check 
out the image below to see all valid moves for a knight 
piece that is placed on one of the central squares.

Example

    For cell = "a1", the output should be
    chessKnight(cell) = 2.

    For cell = "c2", the output should be
    chessKnight(cell) = 6.
"""

cell = "g6"
if __name__ == '__main__':
    print(chessKnight(cell))
