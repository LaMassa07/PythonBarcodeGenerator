c = 285

def xor_bitwise(n1, n2):
    return n1 ^ n2

def generate_power_of_two(exp):
    if exp >= 0 and exp <= 7:
        return pow(2, exp)
    else:
        t = exp - 8
        n = xor_bitwise(pow(2, 8), c)
        for i in range(t):
            n *= 2
            if n >= 256:
                n = xor_bitwise(n, c)
        return n
