n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))
n4 = float(input('Digite a nota 4: '))
m = (n1+n2+n3+n4)/4
print('A nota média é {}'.format(m))
if m <7:
    print("O aluno foi reprovado pois não atingiu a média")
elif m>=7:
    print("O aluno foi aprovdo")
print('A nota média é {}'.format(m))