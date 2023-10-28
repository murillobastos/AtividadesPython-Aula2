def pesoIdeal(sexo, altura):
  if sexo == "H":
    return (72.7*altura)-58
  else:
    return (62.1*altura)-44.7

s = input("Você é homem ou mulher? (Digite M ou H)")
h = float(input("Digite sua altura: "))

print(pesoIdeal(s.upper(),h))