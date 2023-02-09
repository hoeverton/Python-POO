''' Um edificio possui 15 andares, sendo 14 andares de moradia
e o primeiro andar reservado para o térreo (descrito apenas como "1").

Para que os moradores transitem entre os andares, o edificio dispõe
de um elevador instalado. O elevador não possui restrição de andar e
pode transitar por qualquer andar a qualquer hora.

Descreva um programa para utilização do elevador no edificio.'''

from elevador import Elevador

elevador = Elevador()


while (True):
    andar = int(input('Defina um andar: '))
    resposta = elevador.locomover(andar)
    print(resposta)
    print('--------------------------------')
    