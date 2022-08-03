def main():
    print('Hola, este programa sirve para convertir de libras esterlinas (pounds) a euros')
    dinero = float(input('Por favor ingresa la cantidad de libras a convertir: '))
    convertido = dinero*1.15
    print('{} libras son {} euros'.format(dinero, convertido))



if __name__ == '__main__':
    main()