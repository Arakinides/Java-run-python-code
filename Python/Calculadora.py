import sys
import os

diretório = os.getcwd()
print('Lista de argumentos: ', str(sys.argv))
print('total de argumentos: ', len(sys.argv), ' argumentos')


def addition():
    print("O argumento [0] é :", sys.argv[0])
    print("O argumento [1] é :", sys.argv[1])
    print("O argumento [2] é :", sys.argv[2])
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    soma = int(num1)+int(num2)
    print("A soma de {0} e {1} é {2}".format(num1, num2, soma))


addition()
