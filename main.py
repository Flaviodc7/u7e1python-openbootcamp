import operaciones.sumar as suma
import operaciones.restar as resta
import operaciones.multiplicar as multiplica
import operaciones.dividir as divide

def main():
    sum = suma.suma(4, 5)
    rest = resta.resta(5, 4)
    mult = multiplica.multiplicacion(3, 2)
    div = divide.division(6, 3)
    print(sum)
    print(rest)
    print(mult)
    print(div)



if __name__ == '__main__':
    main()