def calcular_idade(dias: int):
    anos = dias // 365
    meses = (dias % 365) // 30
    resto_dias = dias % 30
    return f"A idade dessa pessoa expressa em anos, meses e dias é: {anos} ano(s) {meses} mes(es) e {resto_dias} dias"


idade = int(input('Informe a idade da pessoa em dias:\n'))
print(calcular_idade(idade))