class Disciplina:
    def __init__(self):
        self.__nome = None
        self.__carga_horaria = None

    def setNome(self, nome):
        self.__nome = nome

    def setCargaHoraria(self, carga_horaria):
        self.__carga_horaria = carga_horaria

    def getNome(self):
        return self.__nome

    def getCargaHoraria(self):
        return self.__carga_horaria


