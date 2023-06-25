def reverse_list(lista):
    longitud = len(lista)
    for i in range(longitud // 2):
        lista[i], lista[longitud - i - 1] = lista[longitud - i - 1], lista[i]
    return lista
assert reverse_list([1, 3, 5]) == [5, 3, 1]
assert reverse_list([7, 2, 9, 4]) == [4, 9, 2, 7]
assert reverse_list([0, 0, 1, 0, 0]) == [0, 0, 1, 0, 0]
def is_palindrome(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]
assert is_palindrome("racecar") == True
assert is_palindrome("level") == True
assert is_palindrome("python") == False
assert is_palindrome("madam") == True
assert is_palindrome("hello") == False
def coin(cambio):
    monedas_25 = cambio // 25
    cambio = cambio % 25
    monedas_10 = cambio // 10
    cambio = cambio % 10
    monedas_5 = cambio // 5
    cambio = cambio % 5
    monedas_1 = cambio
    return [monedas_25, monedas_10, monedas_5, monedas_1]
assert coin(87) == [3, 1, 0, 2]
assert coin(55) == [2, 0, 1, 0]
assert coin(37) == [1, 1, 0, 2]
assert coin(100) == [4, 0, 0, 0]
assert coin(13) == [0, 1, 0, 3]
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
assert factorial(5) == 120
assert factorial(1) == 1
assert factorial(0) == 1
assert factorial(10) == 3628800
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    assert fibonacci(5) == 5
assert fibonacci(4) == 3
assert fibonacci(0) == 0
assert fibonacci(10) == 55