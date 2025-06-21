from PIL import Image, ImageDraw  # type: ignore
from qr_matrix_operations import *



def get_img(qr_matrix):
    #cell size, constant#
    size = 20

    griglia_width = len(qr_matrix)
    griglia_height = len(qr_matrix)

    img = Image.new('RGB', (griglia_width * size, griglia_height * size), 'white')
    draw = ImageDraw.Draw(img)


    for y in range(griglia_height):
        for x in range(griglia_width):
            color = 'black' if qr_code[y][x] == 1 else 'white'
            draw.rectangle(
                [x * size, y * size, (x + 1) * size - 1, (y + 1) * size - 1],
                fill=color
            )
    img.show()



qr_code = insert_function_patterns(generate_matrix(2))
get_img(qr_code)