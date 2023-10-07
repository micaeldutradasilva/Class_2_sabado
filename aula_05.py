# Trabalhando com comprimentos de caracteres
# texto = "18/10/2023"
# comprimento = len(texto)
# print(comprimento)

# ------------------------------------------------ // ------------------------------------------------

# Trabalhado com lista
# lista = [1,2.3,4]
# print(len(lista))

# print(type(texto))

# ------------------------------------------------ // ------------------------------------------------

#Trabalhando com listas fragmentadas
# texto = 'Python'
# print(texto)
# flag = list(texto)
# print(flag)

# ------------------------------------------------ // ------------------------------------------------

# Lista com range
# n = range(1,3)
# print(n)

# ------------------------------------------------ // ------------------------------------------------

# Trabalhando com somas
# lista = [1,2,3,5,6,7,8,9]
# soma = sum(lista)
# print('A soma da lista é:',soma)

# ------------------------------------------------ // ------------------------------------------------

# Trabalhando com mínimo e máximo
# Para boas praticas, devem ser criadas listas com os mesmos tipos de dados
# a serem declarados
# lista = [1,36,145]
# maxi = max(lista)
# mini = min(lista)
# print('O número máximo da lista é:',maxi)
# print('O número mínimo da lista é:',mini)

# ------------------------------------------------ // ------------------------------------------------

# Ordenando uma lista do menor para o maior
# lista0 = ['z','e','r','t','a','c','w','y']
# lista = [56,566,7878,15,1,0,89,10]
# organize = sorted(lista0)
# organize2 = sorted(lista)
# print(organize,organize2)

# for i in range(0,51,2):
#     print(i)
    
# ------------------------------------------------ // ------------------------------------------------

# Usando 'for' para printar uma palavra ordenada na sequência

# world = 'Python'
# for i in world:
#     print(i)

# ------------------------------------------------ // ------------------------------------------------

# Trabalhando com for e listas
# lista = ['Maçã','Banana','Uva','Melância']

# for i in lista:
#     print(f'{i[0]}{i[1]}{i[2]}')

# ------------------------------------------------ // ------------------------------------------------

# Trabalhando com dicionários

# name = {
#     'nome': 'Julio',
#     'idade': 18,
#     'endereco': 'rua 10'
# }

# for i,i2 in name.items():
#     print(f'{i} : {i2}') 

# ------------------------------------------------ // ------------------------------------------------

# trabalhando com matriz

matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(matriz[0])

# Loops alinhados

for i in matriz:
    for n in i:
        print(n)