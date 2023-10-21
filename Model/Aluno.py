from Model.Pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self):
        # Construtor da classe pai (Pessoa)
        super().__init__()
        self.__matricula = None

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def getMatricula(self):
        return self.__matricula
