print ('Olá! Bem vindo à calculadora de idade, para começar siga os passos abaixo')

nome= str(input('Digite o seu nome: '))
print (f'Perfeito! Olá {nome}, seja bem vindo ao programa!')
idade=int(input('Qual sua idade atual? '))
idade2 = int(input(f'Entendi, e quantos anos no futuro você quer calcular? '))

print(f'Sua idade daqui a {idade2} anos vai ser de {idade+idade2} anos!')
