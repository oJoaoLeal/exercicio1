class Pessoa:
    def __init__(self):
        self.__nome = None
        self.__dataNascimento = None

    def setNome(self, nome):
        self.__nome = nome

    def setDataNascimento(self, data_nascimento):
        self.__dataNascimento = data_nascimento

    def getNome(self):
        return self.__nome

