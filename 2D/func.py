from encoding_mode import *

version = 0
mode = "..."
error = "..."
data = "..."

MIN_VERSION = 1
MAX_VERSION = 40


count = {
    "N": [10, 12, 14],
    "A": [9, 11, 13],
    "B": [8, 16, 16],
    "K": [8, 10, 12]
}

qr_final_data_array = []

def cls():
    print("\033c", end="")

def monitor():
    cls()

    t = f"""
    \033[37m░██████╗░██████╗░░░░░░░░█████╗░░█████╗░██████╗░███████╗\033[0m
    \033[37m██╔═══██╗██╔══██╗░░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝\033[0m
    \033[37m██║██╗██║██████╔╝█████╗██║░░╚═╝██║░░██║██║░░██║█████╗░░\033[0m           \033[96m[v1.0]\033[0m
    \033[37m╚██████╔╝██╔══██╗╚════╝██║░░██╗██║░░██║██║░░██║██╔══╝░░\033[0m     \033[90m[By Maso&Co]\033[0m
    \033[37m░╚═██╔═╝░██║░░██║░░░░░░╚█████╔╝╚█████╔╝██████╔╝███████╗\033[0m
    \033[37m░░░╚═╝░░░╚═╝░░╚═╝░░░░░░░╚════╝░░╚════╝░╚═════╝░╚══════╝\033[0m

    \033[37m░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░\033[0m
    \033[37m██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗\033[0m
    \033[37m██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝\033[0m
    \033[37m██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗\033[0m
    \033[37m╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║\033[0m
    \033[37m░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝\033[0m
    
    \033[32m
    [1] Version ({version})             
    [2] Data mode ({mode})              
    [3] Error correction level ({error})
    [4] DATA
    [5] PRINT\033[0m

    \033[91m[6] Help \033[0m

    """



    print(t)


def change(i: int):
    global version, mode, error, data

    if i == 1:
        while version < MIN_VERSION or version > MAX_VERSION:
            try:
                version = int(input(f"Choose your QR-CODE version (between {MIN_VERSION} and {MAX_VERSION})\n"))
            except ValueError:
                print(f"\nIt must be a number between {MIN_VERSION} and {MAX_VERSION}")

    elif i == 2:
        while mode not in ["A", "N", "B", "K"]:
            try:
                mode = input("Choose your QR-CODE mode:\nA = Alfanumeric\nN = Numeric\nB = Byte\nK = Kanji\n")
            except:
                pass
    
    elif i == 3:
        pass

    elif i == 4:
        data = input()




def data_type_bits():
    global mode, qr_final_data_array

    if mode == "N":
        m = [0, 0, 0, 1]
    elif mode == "A":
        m = [0, 0, 1, 0]
    elif mode == "B":
        m = [0, 1, 0, 0]
    elif mode == "K":
        m = [1, 0, 0, 0]

    for b in m:
        qr_final_data_array.append(b)


#se si bagga, zè sbaglià (il PC)
def char_count_bits():
    global data, mode, qr_final_data_array

    l = len(data)
    v = 0 if (version in range(1, 9)) else 1 if (version in range(10, 26)) else 2
    tot = count[mode][v]
    n_bin = [int(b) for b in f"{l:0{tot}b}"]
    qr_final_data_array.extend(n_bin)



def encode_data():
    global mode, data, qr_final_data_array

    if mode == "N":
        e = numeric_mode(data)
    elif mode == "A":
        e = numeric_mode(data)
    elif mode == "B":
        e = numeric_mode(data)
    else:
        #I don't feel like programming the kanji
        pass

    while len(e)%8 != 0:
        e.append(0)