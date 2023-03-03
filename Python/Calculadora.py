import sys
import os

# Retorna o diretório de trabalho
diretório = os.getcwd()

# Mostra as vereáveis importadas do java
print('Lista de argumentos: ', str(sys.argv))
print('total de argumentos: ', len(sys.argv), ' argumentos')

# Inicia a função de mostrar separadamente as vareáveis e somar
def addition():

    for i in range(len(sys.argv)):
        print("O argumento [{0}] é : {1}".format(i, sys.argv[i]))

    # Faz o calculo
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    soma = int(num1)+int(num2)

    # Escreve na tela
    print("A soma de {0} e {1} é {2}".format(num1, num2, soma))


addition()
