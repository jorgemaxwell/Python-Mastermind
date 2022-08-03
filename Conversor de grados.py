def main():
    print('Bienvenido al conversor de temperatura, este programa convierte de grados fahrenheit a Centigrados')
    temp = float(input('Por favor ingrese la temperatura que desea convertir: '))
    val= (temp-32)*(5/9)
    print('{} grados fahrenheit equivale a  {} grados centigrados'.format(temp, val))

if __name__ == '__main__':
    main()
