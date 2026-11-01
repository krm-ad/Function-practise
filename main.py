# 1. print_symbol(n, s): напечатать символ n раз
def print_symbol(n, s):
    for i in range(n):
        print(s, end='')
    print()

print_symbol(5, '*')

# 1.1 draw(n, a, b): чередовать два символа (слайд 6)
def draw(n, a, b):
    for i in range(n):
        print(a if i % 2 == 0 else b, end='')
    print()

draw(10, '*', '-')
draw(5, 'A', 'B')

# 2. draw_rectangle(n, m, s): прямоугольник n x m
def draw_rectangle(n, m, s):
    for i in range(n):
        print(s * m)

draw_rectangle(4, 5, '*')

# 3. drawFrame(n, m): пустая рамка
def drawFrame(n, m):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * m)
        else:
            print('*' + ' ' * (m - 2) + '*')

drawFrame(6, 5)

# 4. sum двух чисел (слайд 9)
def sum2(a, b):
    return a + b

print(sum2(4, 5))

# 5. divisors(n): количество делителей
def divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

print(divisors(12))
print(divisors(25))

# 6. is_prime(n): простое число или нет
def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count == 2

print(is_prime(11))
print(is_prime(12))

# 7. Все простые числа на отрезке [A, B]
a, b = 100, 200
for i in range(a, b + 1):
    if is_prime(i):
        print(i, end=' ')
print()

# 8. Следующее простое число после n
def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n

print("Next prime number is:", next_prime(20))
print("Next prime number is:", next_prime(7))

# 9. count_evens(a, b): количество чётных от A до B
def count_evens(a, b):
    count = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            count += 1
    return count

print("Number of evens between 10 and 25:", count_evens(10, 25))

# 10. gcd(a, b): наибольший общий делитель
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("GCD =", gcd(24, 36))