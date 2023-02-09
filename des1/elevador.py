class Elevador:

    def __init__(self):
        self.__andar = 1

    def locomover(self, andar):
        if (andar < 1 or andar > 15):
           return self.__mensagem_de_erro()
        else: 
         return self.__alter_andar(andar)


    def __mensagem_de_erro(self):
        return 'Andar incorreto!'  

    def __alter_andar(self,andar):
        self.__andar = andar
        if (andar == 1):
            return self.__mensagem_terreo()
        else:
            return self.__apresentar_info_usuario()



    def __apresentar_info_usuario(self):
        return 'Elevador indo para {}° andar'.format(self.__andar) 

    def __mensagem_terreo(self):
        return print('Elevador indo para terreo')     