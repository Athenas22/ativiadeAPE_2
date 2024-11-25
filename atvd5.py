soma = 0

for i in range(2):
    nota = int(input('Digite suas notas:'))

    while(nota < 0 or nota > 10):
        print('Notas inválidas!')
        nota = int(input('Digite suas notas:'))

    soma += nota  

media = soma / 2  
print(f'A média das notas é: {media}')

    