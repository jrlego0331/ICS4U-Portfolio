def setEffectTile(len, direction, x, y):
    """
    locates where effect tiles should be placed

    len: length of match
    direction: 'vertical' or 'horizontal'
    x, y: location of gem in the match
    no return value.
    """

    for i in range(len):
        if direction == 'horizontal':
            matrix[x + i][y] = -effectTileCount
        elif direction == 'vertical':
            matrix[x][y + i] = -effectTileCount


def findMatch(row, column, x, y): # row/column for size of matrix
    """
    tally scores based on the length of a match

    row, column: size of matrix
    x, y: location of gem in the match
    """

    # matches in a row
    if matrix[x][y] >= 0 and x + 2 < row and matrix[x][y] == matrix[x + 1][y] == matrix[x + 2][y]:
        firstGem = matrix[x][y]
        n = 0
        # count number of gems in the match
        while x + n < row and matrix[x + n][y] == firstGem:
            n += 1
        setEffectTile(n, 'horizontal', x, y)
        track.value += n * (n - 2) * track.additions
        track.validMove = True

    # matches in a column
    if matrix[x][y] >= 0 and y + 2 < column and matrix[x][y] == matrix[x][y + 1] == matrix[x][y + 2]:
        firstGem = matrix[x][y]
        n = 0
        # count number of gems in the match
        while y + n < column and matrix[x][y + n] == firstGem:
            n += 1
        setEffectTile(n, 'vertical', x, y)
        track.value += n * (n - 2) * track.additions
        track.validMove = True


# call function: insert in the loop
findMatch(len(matrix), len(matrix[x]), x, y)