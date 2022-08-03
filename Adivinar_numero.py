import random
def main():
    print('Hola, el objetivo de este juego es que adivines el numero que tengo en memoria (del 1 al 5) ')
    intentos = int(input('Cuantos intentos deseas? '))
    rand = random.randint(1,5)
    num= 1000
    while rand != num:
        num = int(input('Por favor ingresa tu número del 1 al 5 '))
        if rand != num:
            print('Te equivocaste, intentalo nuevamente ')
            intentos -= 1
            if intentos == 0:
                print('GAME OVER, el número ganador era {} '.format(rand))
        else:
            print('felicidades, tu numero era {} y el numero en memoria era {} , acertaste!'.format(num,rand))

if __name__== '__main__':
    main()