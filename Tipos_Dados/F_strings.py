"""
'f-strigs' 
são uma maneira simples e eficiente de formatar strings.
Permitem incluir expressões dentro de uma string prefixada por f ou F, usando chaves {}. 
Exemplo:
"""
nome = 'Dayene Santos'
altura = 1.64
peso = 48
imc = peso / (altura*altura)

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos,'
linha_3 = f'e seu imc é de {imc}'
print(linha_1)
print(linha_2)
print(linha_3)