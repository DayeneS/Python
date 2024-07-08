"""
Python = Linguagem de programação
Tipo de tipagem = Dinâmica/Forte
Str -> string = texto
Strings = são textos que estão dentro de aspas
DocString = Usar as três aspas duplas antes e depois de determinado texto
permite escrever o que precisar que a linguagem irá "ignorar" os comandos, 
e esse espaço pode ser usado como uma documentação.
Escape -> '\ ou r' = quando é necessário que o interpretador 'pule' alguma parte do texto. 

"""
'''
O uso de aspas simples pode ser usado da mesma maneira, mas lembrando que 
devemos manter um padrão, ou seja, definir o uso de aspas duplas ou simples.
'''
# Aspas simples
print('Dayene')

# Aspas duplas
print("Dayene")

# Escape  
print("Dayene \"Dos\"Santos")

#r
print(r"Dayene \"Dos\"Santos")
'''
Boas práticas sobre o uso de escape, inverta as aspas para que o seu código
flua melhor, ou seja, se estiver usando aspas duplas insira o texto dentro de aspas simples, 
e vice-versa.
'''
print("Dayene 'Dos' Santos")

# Mensagem precedida de hastag não é reproduzida no código; ela pode ser usada antes,
print(123) # depois do código,
# ou abaixo, como se fosse um comentário
print(456) 
