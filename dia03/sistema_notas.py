print ('Bem vindo à calculadora de média!')
nome = input('digite o seu nome: ')
try:
  print (f'Bem vindo, {nome}, digite abaixo suas notas: ')
  nota1 = float(input('Digite a sua primeira nota: '))
  nota2 = float(input('Digite a sua segunda nota: '))
  if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
        print("As notas devem estar entre 0 e 10.")
  else:
    media = (nota1+nota2)/2
    print (f'sua média é:{round(media,2)}')
    if  media >=7:
      print(f'Parabéns! Você foi aprovado com média {media}.')
    elif 5<= media <7:
      print('Você está em recuperação')
    elif media<5:
      print('Infelizmente, você foi reprovado.')
except ValueError:
    print('Digite um número válido!')
