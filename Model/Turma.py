class Turma:
    def __init__(self):
        self.__codigo = None
        self.__disciplina = None  # Associação: Cada Turma recebe uma única Disciplina
        self.__aluno = []  # Associação: Turma recebe uma lista de objetos "Aluno"
        self.__professor = None  # Associação: Cada turma recebe um único objeto "Professor"

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def setDisciplina(self, disciplina):
        self.__disciplina = disciplina

    def addAluno(self, aluno):
        self.__aluno.append(aluno)

    def setProfessor(self, professor):
        self.__professor = professor

    def getCodigo(self):
        return self.__codigo

    def getDisciplina(self):
        return self.__disciplina

    def getAluno(self):
        return self.__aluno

    def getProfessor(self):
        return self.__professor

    def remove_aluno(self, aluno):
        if aluno in self.__aluno:
            self.__aluno.remove(aluno)
