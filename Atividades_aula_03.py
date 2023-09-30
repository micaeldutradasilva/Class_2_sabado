# ----------- Questions -----------
# 1- Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.

# name = input("What 's your name: ")
# print("My name is: ", name, ", let 's go question:")
# number = int(input("Type a number: "))
# double_multiplication= number * number
# print("This number is: ")
# print(double_multiplication)

# 2- Crie duas variáveis para armazenar seu primeiro nome e sobrenome. 
# Em seguida, concatene-as para formar seu nome completo e exiba o resultado.

# fist_name = input("What 's your fist name: ")
# sub_name = input("What 's yout second name: ")
# print("My name is: ", fist_name, sub_name)

# 3- Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis.
# Realize a concatenação desses números como strings e exiba o resultado.

# name = input("What 's your name: ")
# print("Hello", name, "Let 's go guy")
# number_first = int(input("Type a fist number: "))
# number_second = int(input("Type a second number: "))
# print("This number is:",number_first, "and", number_second)

# 4- Crie uma variável para armazenar a palavra "Python". 
# Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.

# name = input("What 's your name: ")
# print("Hello! Mr. ", name, ", go to your class in pyhton!")

# word = "Python"
# number = int(input("Enter with a number: "))
# print("A word is: ")
# print(word, number)

# 5- Declare uma variável contendo uma frase. 
# Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.

# name = input("What 's your name:")
# print("Hello, ", name, "!")
# age = input("How old are you:")
# my_address = input("What 's your address:")
# job = input("What 's your job:")
# print("Hello!")
# print("My name is", name, ", i'm", age, "years old", ", i live in", my_address, ", i'm work with", job)

# 6- Crie três variáveis para armazenar a quantidade de horas, minutos e segundos. 
# Concatene esses valores para formar uma mensagem de tempo no formato "hh:mm:ss".

# print("Hello, guys!")
# hours = input("Type with hours:")
# minutes = input("Type with minutes:")
# seconds = input("Type with seconds")
# print(f'{hours}:{minutes}:{seconds}')

# Usando biblioteca de data e hora:
# from datetime import datetime
# data_atual_hora = datetime.today()
# data = data_atual_hora.strftime('%H:%M:%S')
# print(data)

# 7- Declare duas variáveis com números de telefone, incluindo um código de área e o número principal. Concatene esses valores para formar um número de telefone completo.

# ddd = input("Type it here a DDD:")
# telephone_number = input("Type it here a Telephone number:")
# print(f'({dd1d}) 9 {telephone_number}')

# 8- Crie uma lista de ingredientes para uma receita. Use concatenação para formar uma única string que liste os ingredientes separados por vírgulas.

# lista_de_compras = ['Frutas,', 'Whey protein,', 'Creatina']
# print(lista_de_compras[0],lista_de_compras[1],lista_de_compras[2])

# 9- Peça ao usuário para digitar três adjetivos e armazene-os em variáveis. Em seguida, use essas palavras para criar uma frase concatenada que descreve algo interessante.

# adjetivo_one = input("Digite o primeiro adjetivo:")
# adjetivo_two = input("Digite o segundo adjetivo:")
# adjetivo_three = input("Digite o terceiro adjetivo:")
# print(f'Essa viagem é {adjetivo_one}, gosto muito quando você é {adjetivo_two} e, você faz {adjetivo_three}')

# Explicação
# senha_digitada = input("Dgite uma senha: ")
# name = input("Digite seu nome: ")
# senha = "1234"
# if senha == senha_digitada and name == "Micael":
#     print("Acesse, você digitou corretamente")
# else:
#     print(f'Não pode acessar, poreuqe você digitou {senha_digitada} ou {name} incorretamente.')

# 1- Crie uma condição para comparar idades: 45 e 18 -  QUAL É MENOR E QUAL É MAIOR?

# maior = input("Type it first number: ")
# menor = input("Type it second number: ")
# if maior > menor:
#     print(f'Numero maior é: {menor} e número menor é: {maior}')
# else:
#     print(f'Número maior é: {maior} e número menor é: {menor}')

# 2- Crie um sistema para permitir a verificação de menores em um show

# name = input("Digite o nome do fã:")
# print(f'Olá {name}!')
# idade = int(input("Digite a idade do fã"))
# if idade >= 18:
#     print(f'Pode entrar, curta o show!')
# else:
#     print(f'Barrado, fã é menor que 18 anos!')

# 3- Crie um algoritmo que permita a entrada de 3 notas de alunos, utilize o bloco de código if() para verificar se o aluno passou.

# Sistema escolar de notas
numero_alunos = int(input("Digite quantidade de alunos a serem computados:"))

for i in range(numero_alunos):
    name = input("Digite o nome do aluno")
    nota = int(input("Digite a nota do aluno:"))
    if nota >= 6:
        print(f'{name} foi aprovado!')
    else:
        print(f'{name} foi reprovado!')
