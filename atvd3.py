print ('Digite o tipo de combustível que você deseja:\n Alcool - 1\n Gasolina - 2\n Diesel - 3\n Fim - 4\n')

comb=0
alcool=0
gasolina=0
diesel=0

while (comb !=4):
     comb = input(int('Digite o tipo de combustível que você deseja:\n Alcool - 1\n Gasolina - 2\n Diesel - 3\n Fim - 4\n'))

     if comb == 1:
        alcool += 1
     if comb ==2:
        diesel += 1
     if comb == 3:
        gasolina += 1
     if comb == 4:
        print ('Muito Obrigado!')
     if (comb > 4) :
        print ('Código inválido')

print (f"Alcool\n' {alcool}, 'Diesel\n' {diesel}, 'Gasolina\n' {gasolina}")
    
        