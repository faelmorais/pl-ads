def inverter(text: str):
    return text[::-1]

frase = input('Digite uma frase: ')
print(f'Essa é a sua frase invertida: {inverter(frase)}')