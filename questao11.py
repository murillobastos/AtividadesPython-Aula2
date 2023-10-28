peso = float(input("Digite o peso do peixe: (Para parar digite 0) "))
excesso = 0

while peso != 0:
  if peso == 0:
    break
  if peso > 50:
    excesso = (peso-50) + excesso
  peso = float(input("Digite o peso do peixe: (Para parar digite 0) "))
  
multa = excesso * 4
print(f"O valor da multa é de R${multa}")