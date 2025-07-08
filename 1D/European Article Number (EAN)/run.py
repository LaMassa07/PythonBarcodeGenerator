from PIL import Image, ImageDraw # type: ignore


byte_guard = [1, 0, 1]
byte_c_guard = [0, 1, 0, 1, 0]

barcode_codes = {
    "left": {
        "forward": {
            "0001101": 0,
            "0011001": 1,
            "0010011": 2,
            "0111101": 3,
            "0100011": 4,
            "0110001": 5,
            "0101111": 6,
            "0111011": 7,
            "0110111": 8,
            "0001011": 9,
        },
        "reverse": {
            0: "0001101",
            1: "0011001",
            2: "0010011",
            3: "0111101",
            4: "0100011",
            5: "0110001",
            6: "0101111",
            7: "0111011",
            8: "0110111",
            9: "0001011",
        }
    },
    "right": {
        "forward": {
            "1110010": 0,
            "1100110": 1,
            "1101100": 2,
            "1000010": 3,
            "1011100": 4,
            "1001110": 5,
            "1010000": 6,
            "1000100": 7,
            "1001000": 8,
            "1110100": 9,
        },
        "reverse": {
            0: "1110010",
            1: "1100110",
            2: "1101100",
            3: "1000010",
            4: "1011100",
            5: "1001110",
            6: "1010000",
            7: "1000100",
            8: "1001000",
            9: "1110100",
        }
    }
}


def draw_barcode(s):
    bar_width = 3
    bar_height = 100
    quiet_margin = 50  # spazio bianco sopra e sotto

    total_height = bar_height + quiet_margin * 2
    total_width = (len(s) + 30) * bar_width

    x = 50

    img = Image.new('RGB', (total_width, total_height), 'white')
    draw = ImageDraw.Draw(img)

    for bit in s:
        color = 'black' if bit == 1 else 'white'
        draw.rectangle(
            [x, quiet_margin, x + bar_width - 1, quiet_margin + bar_height],
            fill=color
        )
        x += bar_width

    img.show()


def main():
    s = input("inserisci il testo:\n---> ")
    s_array = [int(c) for c in s]

    
    byte_array = []
    for i in byte_guard:
        byte_array.append(i)


    if len(s_array) % 2 == 0:
        pass
    else:
        s_array.append(0) 
    print(s_array)

    b = barcode_codes["left"]["reverse"].get(0)
    for bit in b:
        byte_array.append(int(bit))
    for i in range(len(s_array)//2):
        b = barcode_codes["left"]["reverse"].get(s_array[i])
        for bit in b:
            byte_array.append(int(bit))
    for i in byte_c_guard:
        byte_array.append(i)
    for i in range(len(s_array)//2, len(s_array)):
        b = barcode_codes["right"]["reverse"].get(s_array[i])
        for bit in b:
            byte_array.append(int(bit))
    
    

    even = sum(s_array[i] for i in range(0, len(s_array), 2))
    odd = sum(s_array[i] for i in range(1, len(s_array), 2))
    tot = (3*odd) + even
    tot_partial = tot

    while tot_partial % 10 != 0:
        tot_partial += 1
    
    crc = tot_partial - tot

    b = barcode_codes["right"]["reverse"].get(crc)
    for bit in b:
        byte_array.append(int(bit))


    for i in byte_guard:
        byte_array.append(i)



    print(byte_array)
    draw_barcode(byte_array)




#main#
main()