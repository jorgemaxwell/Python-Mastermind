def run():
    print("este programa te dira cual es el número menor y cual es el número mayor")
    num1= int(input("por favor ingresa el primer valor "))
    num2= int(input('Por favor ingresa el segundo valor '))
    if num1 > num2:
        num1=str(num1)
        print('el numero mayor es ' + num1)
    else:
        num2=str(num2)
        print('el numero mayor es ' + num2)
if __name__ == '__main__':
    run()

