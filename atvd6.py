soma = 0
qtdidades = 0

while(1):
        
        idade = int(input('Digite as idades.Coloque um número negativo para encerrar o programa:'))
        
        if (idade < 0):
         print('Programa encerrado!')
         break

        soma += idade
        qtdidades += 1

if (qtdidades > 0):
  media = soma/qtdidades


print(f'A média das idades é: {media:.2f}')
