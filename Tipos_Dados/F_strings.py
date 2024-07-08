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

a = 'AAAA'
b = 'BBBB'
c = 1.1
#string = 'a={} b={} c={:.2f}'
#string = 'a={0} b={1} c={2:.2f}'
string = 'b={1} a={0} a={0} a={0} c={2:.2f}'
formato = string.format(a, b, c)
#print(formato)
#ou
#string = 'a={} b={} c={:.2f}'
string = 'a={nome1} b={nome2} c={nome3:.2f}'
#string = 'b={1} a={0} a={0} a={0} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c)
print(formato)