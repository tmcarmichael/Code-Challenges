def chessBoardCellColor(cell1, cell2):
    row1, row2 = ord(cell1[0]), ord(cell2[0])
    col1, col2 = int(cell1[1]), int(cell2[1])
    return (row1 %2 == col1 %2) == (row2 %2 == col2 %2)

"""
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

    For cell1 = "A1" and cell2 = "C3", the output should be
    chessBoardCellColor(cell1, cell2) = true.

    For cell1 = "A1" and cell2 = "H3", the output should be
    chessBoardCellColor(cell1, cell2) = false.

"""

cell1 = "A1"
cell2 = "H3"
if __name__ == '__main__':
    print(chessBoardCellColor(cell1, cell2))
