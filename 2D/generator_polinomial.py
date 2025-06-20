from power_of_two import generate_power_of_two
from polinomial_multiplication import multiplication


ec_codewords = {
    "L": 10,
    "M": 16,
    "Q": 22,
    "H": 28
}



#(x - ɑ^0) ... (x - ɑ^n-1)#
def generate_polinomial(ERROR_LEVEL):
    n = ec_codewords[ERROR_LEVEL]

    p_final = [1, 1]

    for i in range(1, n):
        p_final = multiplication(p_final, [1, generate_power_of_two(i)])


    return p_final


#print(generate_polinomial("L"))


