from func import *


def main():
    monitor()

    #configuration
    i = 0 
    while True:
        monitor()
        try:
            i = int(input())
        except ValueError:
            continue

        if i in range(1, 5):
            change(i)
        elif i == 5:
            # print
            break
    
    #insert the data type bits into the final array
    data_type_bits()


    char_count_bits()


    



main()