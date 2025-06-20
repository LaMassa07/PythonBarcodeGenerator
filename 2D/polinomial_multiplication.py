from log import log2
from power_of_two import generate_power_of_two

Debug = False

def multiplication(p1, p2):
    coeff_p1 = p1
    coeff_p2 = p2

    exp_p1 = []
    exp_p2 = []


    for i in range(len(p1)):
        exp_p1.insert(0, i)
    for i in range(len(p2)):
        exp_p2.insert(0, i)

    #debug: set it to false!!
    if Debug:
        print(coeff_p1)
        print(exp_p1)
        print(coeff_p2)
        print(exp_p2)

    coeff_res = []
    exp_res = []

    for n in range(len(coeff_p1)):
        n1 = coeff_p1[n]
        for m in range(len(coeff_p2)):
            n2 = coeff_p2[m]

            r = n1*n2
            if r >= 256:
                l = log2(r)
                r = generate_power_of_two(l)

            coeff_res.append(r)
            exp_res.append(exp_p1[n] + exp_p2[m])


    i = 0

    while True:
        try:
            if exp_res[i] == exp_res[i+1]:
                exp_res.pop(i+1)
                coeff_res[i] = coeff_res[i] + coeff_res[i+1]
                coeff_res.pop(i+1)
            else:
                pass
            i += 1
        except:
            break

    if Debug:
        print(exp_res)
        print(coeff_res)
    

    return coeff_res






#print(multiplication([1, -3, 2], [1, -4]))