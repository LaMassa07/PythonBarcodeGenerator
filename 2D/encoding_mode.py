#Total Number of Data Codewords for this Version and EC Level#
codewords = {
    "L": 34,
    "M": 28,
    "Q": 22,
    "H": 16
}

#char to value#
ctv = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 18,
    'J': 19,
    'K': 20,
    'L': 21,
    'M': 22,
    'N': 23,
    'O': 24,
    'P': 25,
    'Q': 26,
    'R': 27,
    'S': 28,
    'T': 29,
    'U': 30,
    'V': 31,
    'W': 32,
    'X': 33,
    'Y': 34,
    'Z': 35,
    ' ': 36,
    '$': 37,
    '%': 38,
    '*': 39,
    '+': 40,
    '-': 41,
    '.': 42,
    '/': 43,
    ':': 44
}



def numeric_mode(data):
    output = []
    numbers = []
    for i in range(0, len(data), 3):
        numbers.append(int(data[i:i+3]))

    for n in numbers:
        bits = bin(n)[2:].zfill(8)
        output.extend([int(b) for b in bits])

    return output


def alfanumeric_mode(data):
    output = []
    letters = []
    data = data.upper()
    if len(data)%2 != 0:
        last = data[-1]
        data = data[:-1]

    for i in range(0, len(data), 2):
        letters.append(data[i:i+2])
    for l in letters:
        l1 = l[0]
        l2 = l[1]

        L1 = ctv[l1]
        L2 = ctv[l2]

        n = (L1*45) + L2

        bits = bin(n)[2:].zfill(11)
        output.extend([int(b) for b in bits])  

    try:
        l = ctv[last]
        bits = bin(l)[2:].zfill(6)
        output.extend([int(b) for b in bits])
    except:
        pass
    
    return output


#not ISO-8859-1, i'm using UTF-8#
def byte_mode(data):
    output = []
    for l in data:
        bits = bin(ord(l))[2:].zfill(8)
        output.extend([int(b) for b in bits])
    
    return output
