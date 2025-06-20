from generator_polinomial import generate_polinomial
from polinomial_long_division import division

def get_rs_values(data, ERROR_LEVEL):
    generator_polinomial = generate_polinomial(ERROR_LEVEL)

    codewords = division(data, generator_polinomial)

    return codewords
