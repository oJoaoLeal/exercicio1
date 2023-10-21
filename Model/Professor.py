from Model.Pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self):
        # Construtor da classe pai (Pessoa)
        super().__init__()
        self.__departamento = None

    def setDepartamento(self, departamento):
        self.__departamento = departamento

    def getDepartamento(self):
        return self.__departamento
