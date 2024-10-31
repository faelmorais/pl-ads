import math

def e_primo(n: int):
    if n <= 1:
        return False

    final = int(math.sqrt(n) + 1)
    for i in range(2, final):
        if n % i == 0:
            return False
    return True

for valor in range(1, 101):
    print(f'{valor} é primo') if e_primo(valor) else print(f'{valor} não é primo')



