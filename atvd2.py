x, y =input("Escreva uma coordenada:").split ()
x, y = int (x), int (y)

while (x != 0 and y != 0):
    if ( x > 0 and y > 0):
        print ('Primeiro quadrante')
        x, y =input("Escreva um número:").split ()
        x, y = int (x), int (y)

    elif (x > 0 and y < 0):
        print ('Quarto quadrante')
        x, y =input("Escreva um número:").split ()
        x, y = int (x), int (y)

    elif (x< 0 and y < 0):
        print ('Terceiro quadrante')
        x, y =input("Escreva um número:").split ()
        x, y = int (x), int (y)
    
    elif ( x < 0 and y > 0):
        print ('Segundo quadrante')
        x, y =input("Escreva um número:").split ()
        x, y = int (x), int (y)






