data = input("data: ")
D = ''.join(format(ord(char), '08b') for char in data)

print(D)