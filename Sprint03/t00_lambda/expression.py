n = int(input('n: '))
a = int(input('a: '))
b = int(input('b: '))

# Only edit the following line
result = (lambda x, y, z: n % a == 0 and n % b == 0)(n, a, b)

print(result)
