# INPUT - ENTRADA DE DADOS DO USUÁRIO
# CÁLCULO DE INDÍCE DE MASSA CORPORAL - IMC

# INFORMAÇÕES DO USUÁRIO (NOME, PESO e ALTURA)
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em M: "))

# CÁLCULO DO IMC
calculo = peso / (altura * altura)

# ANÁLISE DE CATEGORIAS COM BASE NO CÁLCULO DE IMC
if calculo <= 18.5 :
    print(f'{nome}, você está ABAIXO DO PESO')

elif 18.6 <= calculo <= 24.9:
    print(f'{nome}, você está com o PESO NORMAL')

elif 25 <= calculo <= 29.9:
    print(f'{nome}, você está SOBREPESO')

elif 30 <= calculo <= 34.9:
    print(f'{nome}, você está com OBESIDADE GRAU I')

elif 35 <= calculo <= 39.9:
    print(f'{nome}, você está com OBESIDADE GRAU II')

else:
    print(f'{nome}, você está com OBESIDADE GRAU III')

