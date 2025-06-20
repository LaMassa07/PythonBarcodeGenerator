centers = {
    2: [6, 18],
    3: [6, 22]
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


    pos = centers[2]

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