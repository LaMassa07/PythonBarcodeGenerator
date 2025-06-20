from PIL import Image, ImageDraw

size = 20
griglia_width = 25
griglia_height = 25

img = Image.new('RGB', (griglia_width * size, griglia_height * size), 'white')
draw = ImageDraw.Draw(img)



def print_data4(x, y, data):
    offsets = [(1,1), (0,1), (1,0), (0,0)]
    for i in range(4):
        dx, dy = offsets[i]
        color = 'white' if data[i] == 0 else 'black'
        draw.rectangle([
            (x + dx) * size, 
            (y + dy) * size, 
            (x + dx + 1) * size - 1, 
            (y + dy + 1) * size - 1
        ], fill=color)

def print_data8(x, y, data):
    offsets = [(1, 3), (0,3), (1,2), (0,2), (1, 1), (0, 1), (1, 0), (0, 0)]
    for i in range(8):
        dx, dy = offsets[i]
        color = 'white' if data[i] == 0 else 'black'
        draw.rectangle([
            (x + dx) * size, 
            (y + dy) * size, 
            (x + dx + 1) * size - 1, 
            (y + dy + 1) * size - 1
        ], fill=color)

def print_data8_orizz_up(x, y, data):
    offsets = [(3,1), (2,1), (3,0), (2,0), (1,0), (0,0), (1,1), (0,1)]
    for i in range(8):
        dx, dy = offsets[i]
        color = 'white' if data[i] == 0 else 'black'
        draw.rectangle([
            (x + dx) * size, 
            (y + dy) * size, 
            (x + dx + 1) * size - 1, 
            (y + dy + 1) * size - 1
        ], fill=color)

def print_data8down(x, y, data):
    offsets = [(1,0), (0,0), (1,1), (0, 1), (1,2), (0, 2), (1, 3), (0, 3)]
    for i in range(8):
        dx, dy = offsets[i]
        color = 'white' if data[i] == 0 else 'black'
        draw.rectangle([
            (x + dx) * size, 
            (y + dy) * size, 
            (x + dx + 1) * size - 1, 
            (y + dy + 1) * size - 1
        ], fill=color)
        
        
def print_data8_orizz_down(x, y, data):
    offsets = [(3,0), (2,0), (3,1), (2,1), (1,1), (0,1), (1,0), (0,0)]
    for i in range(8):
        dx, dy = offsets[i]
        color = 'white' if data[i] == 0 else 'black'
        draw.rectangle([
            (x + dx) * size, 
            (y + dy) * size, 
            (x + dx + 1) * size - 1, 
            (y + dy + 1) * size - 1
        ], fill=color)



def print_default():
    #BLACK
    #ALLINEATORE ESTERNO
    x_est_tl = [0, 1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 6]
    y_est_tl = [0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 6, 1, 2, 3, 4, 5, 6]
    #ALLINEATORE INTERNO
    x_int_tl = [2, 3, 4, 2, 3, 4, 2, 3, 4]
    y_int_tl = [2, 2, 2, 3, 3, 3, 4, 4, 4]
    #PROPORZIONATORE
    x_prop = [16, 17, 18, 19, 20, 16, 20, 16, 18, 20, 16, 20, 16, 17, 18, 19, 20]
    y_prop = [16, 16, 16, 16, 16, 17, 17, 18, 18, 18, 19, 19, 20, 20, 20, 20, 20]
    #DIMENSIONATORE
    x_dim = [6, 6, 6, 6, 6]
    y_dim = [8, 10, 12, 14, 16]

    

    #DISEGNA GLI  ALLINEATORI E I PROPORZIONATORI/DIMENSIONATORI
    for i in range(0, len(x_est_tl)):
        x0 = x_est_tl[i] * size
        y0 = y_est_tl[i] * size
        x1 = x0 + size - 1
        y1 = y0 + size - 1
        draw.rectangle([x0, y0, x1, y1], fill='black')
    for i in range(0, len(x_int_tl)):
        x0 = x_int_tl[i] * size
        y0 = y_int_tl[i] * size
        x1 = x0 + size - 1
        y1 = y0 + size - 1
        draw.rectangle([x0, y0, x1, y1], fill='black')

    for i in range(0, len(x_est_tl)):
        x0 = x_est_tl[i] * size
        y0 = (y_est_tl[i] + 18) * size
        x1 = x0 + size - 1
        y1 = y0 + size - 1
        draw.rectangle([x0, y0, x1, y1], fill='black')
    for i in range(0, len(x_int_tl)):
        x0 = x_int_tl[i] * size
        y0 = (y_int_tl[i] + 18) * size
        x1 = x0 + size - 1
        y1 = y0 + size - 1
        draw.rectangle([x0, y0, x1, y1], fill='black')

    for i in range(0, len(x_est_tl)):
        x0 = (x_est_tl[i] + 18) * size
        y0 = y_est_tl[i] * size
        x1 = x0 + size - 1
        y1 = y0 + size - 1
        draw.rectangle([x0, y0, x1, y1], fill='black')
    for i in range(0, len(x_int_tl)):
        x0 = (x_int_tl[i] + 18) * size
        y0 = y_int_tl[i] * size
        x1 = x0 + size - 1
        y1 = y0 + size - 1
        draw.rectangle([x0, y0, x1, y1], fill='black')

    for i in range(0, len(x_dim)):
        x0 = x_dim[i] * size
        y0 = y_dim[i] * size
        x1 = x0 + size - 1
        y1 = y0 + size - 1
        draw.rectangle([x0, y0, x1, y1], fill='black')

    for i in range(0, len(x_dim)):
        y0 = x_dim[i] * size
        x0 = y_dim[i] * size
        x1 = x0 + size - 1
        y1 = y0 + size - 1
        draw.rectangle([x0, y0, x1, y1], fill='black')

    for i in range(0, len(x_prop)):
        y0 = x_prop[i] * size
        x0 = y_prop[i] * size
        x1 = x0 + size - 1
        y1 = y0 + size - 1
        draw.rectangle([x0, y0, x1, y1], fill='black')


    y_always_black = 8
    x_always_black = 17

    y0 = x_always_black * size
    x0 = y_always_black * size
    x1 = x0 + size - 1
    y1 = y0 + size - 1
    draw.rectangle([x0, y0, x1, y1], fill='black')


def main():
    DATA = input("type the data (max 511 characters)... \n")

    #START POSITION
    x_cursor = 23
    y_cursor = 23

    #DEFINIZIONE TIPO
    data_type = [0, 0, 1, 0] #alfanumerico
    print_data4(x_cursor, y_cursor, data_type)

    #LUNGHEZZA DATI
    len_data = len(DATA)
    len_data_bin = bin(len_data)[2:]
    len_data_bin = len_data_bin.zfill(8)
    len_data_bin = [int(b) for b in len_data_bin]

    y_cursor -= 4

    print_data8(x_cursor, y_cursor, len_data_bin)

    
    #INSERIMENTO DATI
    char_num = 0
    
    for char in DATA:
        char_num += 1
        d = ''.join(format(ord(c), '08b') for c in char)
        char_array = [int(b) for b in d]
        if char_num == 1 or char_num == 2:
            y_cursor -= 4
            print_data8(x_cursor, y_cursor, char_array)
        if char_num == 3:
            y_cursor -= 2
            x_cursor -= 2
            print_data8_orizz_up(x_cursor, y_cursor, char_array)
        if char_num == 4:
            y_cursor += 2
            print_data8down(x_cursor, y_cursor, char_array)
        if char_num == 5 or char_num == 6:
            y_cursor += 4
            print_data8down(x_cursor, y_cursor, char_array)
        if char_num == 7:
            y_cursor += 4
            x_cursor -= 2
            print_data8_orizz_down(x_cursor, y_cursor, char_array)
        if char_num == 8:
            y_cursor -= 4
            print_data8(x_cursor, y_cursor, char_array)
        















    print_default()
    img.show()

main()