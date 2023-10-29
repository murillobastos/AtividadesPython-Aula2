salario = float(input("Digite o salário atual do colaborador:  "))

limite1 = 280.00
limite2 = 700.00
limite3 = 1500.00
porcentagem1 = 0.20  
porcentagem2 = 0.15  
porcentagem3 = 0.10  
porcentagem4 = 0.05  

if salario <= limite1:
    porcentagem = porcentagem1
elif salario <= limite2:
    porcentagem = porcentagem2
elif salario <= limite3:
    porcentagem = porcentagem3
else:
    porcentagem = porcentagem4

valor_aumento = salario * porcentagem
novo_salario = salario + valor_aumento

print(f"Salário antes do reajuste: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: {porcentagem * 100:.2f}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")