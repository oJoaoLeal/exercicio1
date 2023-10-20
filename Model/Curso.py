class Curso:
    def __init__(self):
        self.__turma = []  # Associação: Curso recebe uma lista de objetos "Turma"
        self.__aluno = []  # Associação: Curso recebe uma lista de objetos "Aluno"

    def addTurma(self, turma):
        self.__turma.append(turma)

    def addAluni(self, aluno):
        self.__aluno.append(aluno)

    def getTurma(self):
        return self.__turma

    def getAluno(self):
        return self.__aluno
