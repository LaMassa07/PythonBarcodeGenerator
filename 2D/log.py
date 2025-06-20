def log2(a):
    log = 0
    while a > 1:
        a = a // 2
        log += 1

    return log
