salHora = float(input("Digite quanto você ganha por hora: "))
hora = int(input("Digite quantas horas trabalhou este mês: "))
salario = (salHora * hora)
salarioIR = salario * 0.11
salarioINSS = salario * 0.08
salarioSindicato = salario * 0.05
salarioLiquido = salario - salarioSindicato - salarioINSS - salarioIR
print(f"Salário bruto: R${salario}")
print(f"Parte do salário paga ao Imposto de Renda: R${salarioIR}")
print(f"Parte do salário paga ao INSS: R${salarioINSS}")
print(f"Parte do salário paga ao sindicato: R${salarioSindicato}")
print(f"Salário líquido: R${salarioLiquido}")


