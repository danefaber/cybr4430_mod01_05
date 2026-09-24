import math
# function that takes a matrix as its input and returns the number of dimensions if a well-formed matrix and Linear Independent, otherwise return False.
def checkLinearIndependence(m1):
    if not isinstance(m1, list) or len(m1) == 0:
        return False

    if not all(isinstance(row, list) for row in m1):
        return False
    cols = len(m1[0])

    if cols == 0:
        return False

    for row in m1:
        if len(row) != cols:
            return False

    rows = len(m1)

    if rows != cols:
        return False

    matrix = [row[:] for row in m1]

    rank = 0

    for col in range(cols):
        pivot = None

        for row in range(rank, rows):
            if abs(matrix[row][col]) > 1e-10:
                pivot = row
                break

        if pivot is not None:
            matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]

            pivot_value = matrix[rank][col]

            for j in range(cols):
                matrix[rank][j] /= pivot_value

            for row in range(rows):
                if row != rank:
                    factor = matrix[row][col]

                    for j in range(cols):
                        matrix[row][j] -= factor * matrix[rank][j]

            rank += 1

    if rank == rows:
        return rows

    return False

# function that takes a matrix as its input and returns the number of dimensions if a well-formed identity matrix, otherwise return False.
def checkIdentity(m1):
    if not isinstance(m1, list) or len(m1) == 0:
        return False

    n = len(m1)

    for row in m1:
        if not isinstance(row, list) or len(row) != n:
            return False

    for i in range(n):
        for j in range(n):
            if i == j:
                if m1[i][j] != 1:
                    return False
            else:
                if m1[i][j] != 0:
                    return False

    return n

# function that returns normalized identity matrix in n dimensions
def getIdentity(n):
    if not isinstance(n, int) or n <= 0:
        return False

    identity = []

    for i in range(n):
        row = []

        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)

        identity.append(row)

    return identity

# function that returns normalized Hadamard matrix in 2 dimensions
def getHadmond():
    value = 1 / math.sqrt(2)

    return [
        [value, value],
        [value, -value]
    ]

def checkHadmond(m1):
    if not isinstance(m1, list) or len(m1) != 2:
        return False

    for row in m1:
        if not isinstance(row, list) or len(row) != 2:
            return False

    value = 1 / math.sqrt(2)

    expected = [
        [value, value],
        [value, -value]
    ]

    for i in range(2):
        for j in range(2):
            if abs(m1[i][j] - expected[i][j]) > 1e-10:
                return False

    return 2