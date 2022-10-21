def p_bin(n):
    c = ''
    while n > 0:
        c = str(n % 2) + c
        n = n//2
    print(c)

def p_oct(n):
    c = ''
    while n > 0:
        c = str(n % 8) + c
        n = n//8
    print(c)

try:
    n = int(input('Введите положительно целое число: '))
except ValueError:
    n = int(input('Это вещественное число. Введите положительно целое число: '))

try:
    b = int(input('Введите систему счисления, в которую хотите перевести число: '))
    if b != 2 and b != 8:
        b = int(input('Перевод возможен только в 2СС, либо в 8СС. Введите систему счисления, в которую хотите перевести число: '))
except ValueError:
    b = int(input('Это вещественное число. Введите положительно целое число: '))
if b == 2:
    p_bin(n)
else:
    p_oct(n)