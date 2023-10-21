class Curso:
    def __init__(self):
        self.__nome = None
        self.__tipo = None
        self.__turma = []  # Associação: Curso recebe uma lista de objetos "Turma"
        self.__aluno = []  # Associação: Curso recebe uma lista de objetos "Aluno"

    def setNome(self, nome):
        self.__nome = nome

    def setTipo(self, tipo):
        self.__tipo = tipo

    def addTurma(self, turma):
        self.__turma.append(turma)

    def addAluno(self, aluno):
        self.__aluno.append(aluno)

    def getNome(self):
        return self.__nome

    def getTipo(self):
        return self.__tipo

    def getTurma(self):
        return self.__turma

    def getAluno(self):
        return self.__aluno
