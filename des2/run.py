
'''Considerando o descritivo do desafio anterior, o edificio
decidiu por implementar 2 elevadores e, desse modo, transportar
mais moradores de forma mais independente.

Descreva um programa para esse novo cenario'''



from models import Elevador
from controller import GerenciadoresDeElevadores

elevador1 = Elevador(1)
elevador2 = Elevador(2)
gerenciadorDeElevadores = GerenciadoresDeElevadores(elevador1, elevador2)

while (True):
    elevadorId = int(input('Em qual elevador vc se encontra?'))
    andar = int(input('Defina um andar: '))
    resposta = gerenciadorDeElevadores.locomover(andar, elevadorId)
    print(resposta)
    print('--------------------------------')