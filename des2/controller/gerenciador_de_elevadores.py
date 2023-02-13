class GerenciadoresDeElevadores:

    def __init__(self,elevador1, elevador2):
        self.__elevadores = [elevador1,elevador2]

    def locomover(self, andar, id):
        if (andar < 1 or andar > 15):
           return self.__mensagem_de_erro()
        else: 
         return self.__filtrar_elevador_e_alterar_andar(andar,id)


    def __filtrar_elevador_e_alterar_andar(self, andar, id):

       for elevador in self.__elevadores:
           if elevador.check_id(id):
               return self.__alter_andar(andar, elevador)

    def __mensagem_de_erro(self):
        return 'Andar incorreto!'  

    def __alter_andar(self, andar, elevador):
        elevador.set_andar(andar)
        if (andar == 1):
            return self.__mensagem_terreo(elevador)
        else:
            return self.__apresentar_info_usuario(elevador)



    def __apresentar_info_usuario(self,elevador):
        return 'Elevador {} indo para {}° andar'.format(elevador.get_id(),elevador.get_andar()) 

    def __mensagem_terreo(self,elevador):
        return print('Elevador {} indo para terreo'. format(elevador.get_id()))     