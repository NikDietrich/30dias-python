print ('Olá! Bem vindo ao validador de maioridade, para começar siga os passos abaixo')

nome = str(input ('Digite o seu nome: '))
print(f'Ótimo, bem vindo {nome}!')
try:
  idade=int(input('Digite a sua idade: '))
  nova_idade = 18-idade
  if idade >= 120 or idade < 0:
    print ('Você é um Highlander? Tente novamente!')
  elif idade >= 18:
    print('Parabéns! Você é maior de idade!')
  elif idade < 18:
    print (f'Você ainda é menor de idade, espere {nova_idade} anos e tente novamente!')
except ValueError:
  print('Você precisa digitar um número!')
