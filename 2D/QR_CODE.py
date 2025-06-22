from PIL import Image, ImageDraw  # type: ignore
from encoding_mode import *
from reed_solomon import get_rs_values
from qr_matrix_operations import *

MAX_VERSION = 6

qr_final_data_array = []
Debug = True


def main(): 
    VERSION = 0
    while VERSION <= 0 and VERSION >= MAX_VERSION:
        VERSION = input(f"choose the version of the QR-Code (MIN: 1, MAX: {MAX_VERSION})\nVERSION: ")


    #MODE SELECTION AND DATA INPUT#
    while True:
        MOD = input("choose the mode:\nN = numeric\nA = alfanumeric\nB = byte\nK = kanji (not working yet)\nMODE: ")       
        if MOD in ["N", "A", "B"]:
            DATA = input("\nenter here your data\nDATA: ")
            break
        else:
            print("invalid mode, please try again...\n")
    
    #NUMERIC MODE#
    if MOD == "N":
        if len(DATA) <= 34:
            while True:
                ERROR = input("choose the error correction level:\nL = low, 7%\nM = medium, 15%\nQ = quartile, 25%\nH = high, 30%\nLEVEL: ")
                if ERROR in ["L", "M", "Q", "H"]:
                    break
                else:
                    print("invalid error correction level, please try again...\n")
        elif len(DATA) <= 48:
            while True:
                ERROR = input("choose the error correction level:\nL = low, 7%\nM = medium, 15%\nQ = quartile, 25%\nLEVEL: ")
                if ERROR in ["L", "M", "Q"]:
                    break
                else:
                    print("invalid error correction level, please try again...\n")
        elif len(DATA) <= 63:
            while True:
                ERROR = input("choose the error correction level:\nL = low, 7%\nM = medium, 15%\nLEVEL: ")
                if ERROR in ["L", "M"]:
                    break
                else:
                    print("invalid error correction level, please try again...\n")
        elif len(DATA) <= 77:
            while True:
                ERROR = input("choose the error correction level:\nL = low, 7%\nLEVEL: ")
                if ERROR in ["L"]:
                    break
                else:
                    print("invalid error correction level, please try again...\n")
        else:
            print("the data input is too long, please type something shorter...\n")

    #ALPHANUMERIC MODE#
    elif MOD == "A":
        if len(DATA) <= 20:
            while True:
                ERROR = input("choose the error correction level:\nL = low, 7%\nM = medium, 15%\nQ = quartile, 25%\nH = high, 30%\nLEVEL: ")
                if ERROR in ["L", "M", "Q", "H"]:
                    break
                else:
                    print("invalid error correction level, please try again...\n")
        elif len(DATA) <= 29:
            while True:
                ERROR = input("choose the error correction level:\nL = low, 7%\nM = medium, 15%\nQ = quartile, 25%\nLEVEL: ")
                if ERROR in ["L", "M", "Q"]:
                    break
                else:
                    print("invalid error correction level, please try again...\n")
        elif len(DATA) <= 38:
            while True:
                ERROR = input("choose the error correction level:\nL = low, 7%\nM = medium, 15%\nLEVEL: ")
                if ERROR in ["L", "M"]:
                    break
                else:
                    print("invalid error correction level, please try again...\n")
        elif len(DATA) <= 47:
            while True:
                ERROR = input("choose the error correction level:\nL = low, 7%\nLEVEL: ")
                if ERROR in ["L"]:
                    break
                else:
                    print("invalid error correction level, please try again...\n")
        else:
            print("the data input is too long, please type something shorter...\n")

    #BYTE MODE#
    elif MOD == "B":
        if len(DATA) <= 14:
            while True:
                ERROR = input("choose the error correction level:\nL = low, 7%\nM = medium, 15%\nQ = quartile, 25%\nH = high, 30%\nLEVEL: ")
                if ERROR in ["L", "M", "Q", "H"]:
                    break
                else:
                    print("invalid error correction level, please try again...\n")
        elif len(DATA) <= 20:
            while True:
                ERROR = input("choose the error correction level:\nL = low, 7%\nM = medium, 15%\nQ = quartile, 25%\nLEVEL: ")
                if ERROR in ["L", "M", "Q"]:
                    break
                else:
                    print("invalid error correction level, please try again...\n")
        elif len(DATA) <= 26:
            while True:
                ERROR = input("choose the error correction level:\nL = low, 7%\nM = medium, 15%\nLEVEL: ")
                if ERROR in ["L", "M"]:
                    break
                else:
                    print("invalid error correction level, please try again...\n")
        elif len(DATA) <= 32:
            while True:
                ERROR = input("choose the error correction level:\nL = low, 7%\nLEVEL: ")
                if ERROR in ["L"]:
                    break
                else:
                    print("invalid error correction level, please try again...\n")
        else:
            print("the data input is too long, please type something shorter...\n")
                
            

    #INSERT THE DATA TYPE BITS INTO THE FINAL ARRAY#
    if MOD == "N":
        mode = [0, 0, 0, 1]
        for b in mode:
            qr_final_data_array.append(b)
    elif MOD == "A":
        mode = [0, 0, 1, 0]
        for b in mode:
            qr_final_data_array.append(b)
    elif MOD == "B":
        mode = [0, 1, 0, 0]
        for b in mode:
            qr_final_data_array.append(b)

    #INSERT THE DATA COUNT BYTES IN THE FINAL ARRAY#
    n = len(DATA)
    count_bits = {
        "N": 10,
        "A": 9,
        "B": 8
    }
    bits = count_bits[MOD]
    n_bin = [int(b) for b in f"{n:0{bits}b}"]
    qr_final_data_array.extend(n_bin)


    #ENCODE THE DATA STRING AND INSERT IN THE FINAL ARRAY#
    if MOD == "N":
        encoded = (numeric_mode(DATA))
    elif MOD == "A":
        encoded = (alfanumeric_mode(DATA))
    elif MOD == "B":
        encoded = (byte_mode(DATA))
    

    while len(encoded)%8 != 0:
        encoded.append(0)
    
    encoded_data = encoded

    patterns = [[1,1,1,0,1,1,0,0], [0,0,0,1,0,0,0,1]]
    i = 0
    while len(encoded) < codewords[ERROR]*8:
        encoded.extend(patterns[i % 2])
        i += 1

    encoded = encoded[:codewords[ERROR]*8]


    #se alla fine da errori, il preblema è il padding di riempimento!!!#
    qr_final_data_array.extend(encoded)
    if Debug:
        print(f"MOD: {MOD}")
        print(f"DATA: {DATA}")
        print(f"ERROR: {ERROR}")
        print(f"LEN: {n}")
        print(f"FINAL: {qr_final_data_array}")


    #ERROR CORRECTION#
    #print(len(data_for_error_correction)%8)
    data_for_error_correction = []
    for i in range(0, len(encoded_data), 8):
        byte = encoded_data[i:i+8]
        val = 0
        for bit in byte:
            val = (val << 1) | bit
        data_for_error_correction.append(val)

    #print(get_rs_values(data_for_error_correction, ERROR))

    
            







    #print
    print_qr_code()



###########
main()