centers = {
    2: [6, 18],
    3: [6, 22],
    4: [6, 26],
    5: [6, 30],
    6: [6, 34],
    7: [6, 22, 38],
    8: [6, 24, 42],
    9: [6, 26, 46],
    10: [6, 28, 50],
    11: [6, 30, 54],
    12: [6, 32, 58],
    13: [6, 34, 62],
    14: [6, 26, 46, 66],
    15: [6, 26, 48, 70],
    16: [6, 26, 50, 74],
    17: [6, 30, 54, 78],
    18: [6, 30, 56, 82],
    19: [6, 30, 58, 86],
    20: [6, 34, 62, 90],
    21: [6, 28, 50, 72, 94],
    22: [6, 26, 50, 74, 98],
    23: [6, 30, 54, 78, 102],
    24: [6, 28, 54, 80, 106],
    25: [6, 32, 58, 84, 110],
    26: [6, 30, 58, 86, 114],
    27: [6, 34, 62, 90, 118],
    28: [6, 26, 50, 74, 98, 122],
    29: [6, 30, 54, 78, 102, 126],
    30: [6, 26, 52, 78, 104, 130],
    31: [6, 30, 56, 82, 108, 134],
    32: [6, 34, 60, 86, 112, 138],
    33: [6, 30, 58, 86, 114, 142],
    34: [6, 34, 62, 90, 118, 146],
    35: [6, 30, 54, 78, 102, 126, 150],
    36: [6, 24, 50, 76, 102, 128, 154],
    37: [6, 28, 54, 80, 106, 132, 158],
    38: [6, 32, 58, 84, 110, 136, 162],
    39: [6, 26, 54, 82, 110, 138, 166],
    40: [6, 30, 58, 86, 114, 142, 170]
}

def generate_matrix(VERSION):
    size = (((VERSION-1)*4)+21)
    print(size)

    qr_matrix = []

    for i in range(size):
        qr_matrix.append([0 for _ in range(size)])

    return qr_matrix


def insert_function_patterns(qr_matrix):
    size = len(qr_matrix)
    
    #X and Y are swiped

    #finder patterns

    #patterns:
    black = [
        # Bordo superiore
        (0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6),
        # Bordo inferiore
        (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6),
        # Bordi laterali centrali
        (1,0), (2,0), (3,0), (4,0), (5,0),
        (1,6), (2,6), (3,6), (4,6), (5,6),
        # Quadrato centrale 3x3
        (2,2), (2,3), (2,4),
        (3,2), (3,3), (3,4),
        (4,2), (4,3), (4,4)
    ]

    white = [
        # Bordo esterno 9x9
        (-1,-1), (-1,0), (-1,1), (-1,2), (-1,3), (-1,4), (-1,5), (-1,6), (-1,7),
        (7,-1), (7,0), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7),
        (0,-1), (1,-1), (2,-1), (3,-1), (4,-1), (5,-1), (6,-1),
        (0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7),
        
        # Già esistenti
        (1,1), (1,2), (1,3), (1,4), (1,5),
        (2,1), (2,5),
        (3,1), (3,5),
        (4,1), (4,5),
        (5,1), (5,2), (5,3), (5,4), (5,5)
    ]



    #first finder:
    for dx, dy in black:
        qr_matrix[dx][dy] = 1
    for dx, dy in white:
        try:
            qr_matrix[dx][dy] = 0
        except:
            pass
    
    #second finder (down, left):
    for dx, dy in black:
        qr_matrix[dx + (size-7)][dy] = 1
    for dx, dy in white:
        try:
            qr_matrix[dx + (size-7)][dy] = 0
        except:
            pass
    
    #third finder (up, right):
    for dx, dy in black:
        qr_matrix[dx][dy + (size-7)] = 1
    for dx, dy in white:
        try:
            qr_matrix[dx][dy + (size-7)] = 0
        except:
            pass


    #patterns:
    black = [(-2,-2), (-2,-1), (-2,0), (-2,1), (-2,2), 
            (-1,-2), (-1,2), 
            (0,-2), (0,2), 
            (1,-2), (1,2), 
            (2,-2), (2,-1), (2,0), (2,1), (2,2), 
            (0,0)]

    white = [(-1,-1), (-1,0), (-1,1), 
            (0,-1), (0,1), 
            (1,-1), (1,0), (1,1)]

    s = len(qr_matrix)
    pos = centers[((s - 21) // 4) + 1]

    for p in pos:
        p1 = p
        for q in pos:
            p2 = q
            if qr_matrix[p1][p2] != 1:
                for dx, dy in black:
                    qr_matrix[dx + p1][dy + p2] = 1
                for dx, dy in white:
                    qr_matrix[dx + p1][dy + p2] = 0
                
            else:
                pass

    #insert timing pattern
    for x in range (6, size - 6):
        qr_matrix[6][x] = 0 if (x % 2) else 1
        qr_matrix[x][6] = 0 if (x % 2) else 1


    #insert black dot
    qr_matrix[size - 8][8] = 1


    return qr_matrix

#insert_function_patterns(generate_matrix(2))