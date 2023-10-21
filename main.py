from Model.Aluno import Aluno
from Model.Curso import Curso
from Model.Disciplina import Disciplina
from Model.Professor import Professor
from Model.Turma import Turma

if __name__ == '__main__':

    aluno1 = Aluno()
    aluno1.setNome("João Victor")
    aluno1.setDataNascimento("13-01-2004")
    aluno1.setMatricula("001443")

    aluno2 = Aluno()
    aluno2.setNome("Jean Lucas")
    aluno2.setDataNascimento("23-11-2003")
    aluno2.setMatricula("001223")

    aluno3 = Aluno()
    aluno3.setNome("Ariel")
    aluno3.setDataNascimento("15-03-2002")
    aluno3.setMatricula("011321")

    aluno4 = Aluno()
    aluno4.setNome("Barra")
    aluno4.setDataNascimento("21-02-2004")
    aluno4.setMatricula("011331")

    professor1 = Professor()
    professor1.setNome("Giácopo")
    professor1.setDataNascimento("15-01-2000")
    professor1.setDepartamento("Exatas")

    professor2 = Professor()
    professor2.setNome("Murilo")
    professor2.setDataNascimento("15-09-2002")
    professor2.setDepartamento("Exatas")

    curso1 = Curso()
    curso1.setNome("Sistemas de Informação")
    curso1.setTipo("Bacharelado")

    curso2 = Curso()
    curso2.setNome("Análise e Desenvolvimento de Sistemas")
    curso2.setTipo("Tecnólogo")

    curso3 = Curso()
    curso3.setNome("Engenharia da Computação")
    curso3.setTipo("Bacharelado")

    turma1 = Turma()
    turma1.setCodigo("001")

    turma2 = Turma()
    turma2.setCodigo("002")

    turma3 = Turma()
    turma3.setCodigo("003")

    turma4 = Turma()
    turma4.setCodigo("004")

    disciplina1 = Disciplina()
    disciplina1.setNome("Algoritmos")
    disciplina1.setCargaHoraria("36h")

    disciplina2 = Disciplina()
    disciplina2.setNome("Orientação a Objetos")
    disciplina2.setCargaHoraria("24h")

    disciplina3 = Disciplina()
    disciplina3.setNome("Estrutura de Dados")
    disciplina3.setCargaHoraria("36h")

    disciplina4 = Disciplina()
    disciplina4.setNome("Sistemas Operacionais")
    disciplina4.setCargaHoraria("40h")

    #  Associação: Curso recebe uma lista de Aluno
    curso1.addAluno(aluno3)
    curso2.addAluno(aluno1)
    curso3.addAluno(aluno4)
    curso1.addAluno(aluno2)

    #  Associação: Curso recebe uma lista de Turma

    curso1.addTurma(turma1)
    curso1.addTurma(turma2)
    curso2.addTurma(turma4)
    curso2.addTurma(turma1)
    curso3.addTurma(turma2)

    # Associação: Turma recebe uma lista de Aluno

    turma1.addAluno(aluno2)
    turma1.addAluno(aluno1)
    turma2.addAluno(aluno4)
    turma3.addAluno(aluno3)
    turma4.addAluno(aluno4)

    # Associação: Turma recebe um único objeto Disciplina

    turma1.setDisciplina(disciplina2)
    turma2.setDisciplina(disciplina4)
    turma3.setDisciplina(disciplina3)
    turma4.setDisciplina(disciplina1)

    # Associação: Turma recebe um único objeto Professor

    turma1.setProfessor(professor1)
    turma2.setProfessor(professor2)
    turma4.setProfessor(professor2)
    turma3.setProfessor(professor1)

    print(f"1) Qual é o nome de um professor de uma turma? \n{turma1.getProfessor().getNome()}")
    print()

    print(f"2) Qual é o nome de todos os alunos de uma turma?")
    print(f"Disciplina: {turma1.getDisciplina().getNome()}")
    print(f"Código: {turma1.getCodigo()}")
    for aluno in turma1.getAluno():
        print(aluno.getNome())
    print()

    print("3) Quais os nomes dos professores que lecionam em alguma turma de um curso?")
    cursos = [curso1, curso2, curso3]
    for curso in cursos:
        print(f"Curso: {curso.getNome()}")
        for turma in curso.getTurma():
            professor = turma.getProfessor()
            print(f"Turma: {turma.getCodigo()}, Professor: {professor.getNome()}")
    print()

    print("4) Quais os nomes dos alunos que estão em alguma turma de um curso?")
    for curso in cursos:
        print(f"Curso: {curso.getNome()}")
        for turma in curso.getTurma():
            print(f"Turma: {turma.getCodigo()}, Alunos:")
            for aluno in turma.getAluno():
                print(aluno.getNome())
    print()

    print("5) Quais os nomes dos alunos que estão registrados em um curso?")
    for curso in cursos:
        print(f"Curso: {curso.getNome()}, Tipo: {curso.getTipo()}")
        print("Alunos:")
        for aluno in curso.getAluno():
            print(aluno.getNome())
    print()

    print("6) Quais as disciplinas que estão em alguma turma de um curso?")
    for curso in cursos:
        print(f"Curso: {curso.getNome()}")
        for turma in curso.getTurma():
            disciplina = turma.getDisciplina()
            print(f"Turma: {turma.getCodigo()}, Disciplina: {disciplina.getNome()}")
    print()

    print("7) Verificar se um aluno está numa turma.")

    def aluno_na_turma(aluno, turma):
        return aluno in turma.getAluno()

    # Verificar se o aluno1 está na turma1
    if aluno_na_turma(aluno1, turma1):
        print(f"{aluno1.getNome()} está na turma {turma1.getCodigo()}.")
    else:
        print(f"{aluno1.getNome()} não está na turma {turma1.getCodigo()}.")
    print()

    print("8) Verificar se um aluno está em um curso.")

    def aluno_no_curso(aluno, curso):
        return aluno in curso.getAluno()


    # Verificar se o aluno1 está no curso1
    if aluno_no_curso(aluno1, curso1):
        print(f"{aluno1.getNome()} está no curso de {curso1.getNome()}.")
    else:
        print(f"{aluno1.getNome()} não está no curso de {curso1.getNome()}.")
    print()

    print("9) Verificar se uma turma está em um curso.")

    def turma_no_curso(turma, curso):
        return turma in curso.getTurma()


    # Verificar se a turma1 está no curso1
    if turma_no_curso(turma1, curso1):
        print(f"A turma {turma1.getCodigo()} está no curso de {curso1.getNome()}.")
    else:
        print(f"A turma {turma1.getCodigo()} não está no curso de {curso1.getNome()}.")
    print()

    print("10) Excluir um aluno de uma turma.")
    # Remover o aluno1 da turma1
    if aluno1 in turma1.getAluno():
        turma1.remove_aluno(aluno1)
        print(f"O aluno {aluno1.getNome()} foi removido da turma {turma1.getCodigo()}.")
    else:
        print(f"O aluno {aluno1.getNome()} não está na turma {turma1.getCodigo()}.")
    print()

    print("11) Excluir uma turma de um curso.")
    # Remover a turma1 do curso1
    if turma1 in curso1.getTurma():
        curso1.remove_turma(turma1)
        print(f"A turma {turma1.getCodigo()} foi removida do curso de {curso1.getNome()}.")
    else:
        print(f"A turma {turma1.getCodigo()} não está no curso de {curso1.getNome()}.")
    print()

    print("12) Excluir um aluno de um curso.")
    # Remover o aluno1 do curso1
    if aluno1 in curso1.getAluno():
        curso1.remove_aluno(aluno1)
        print(f"O aluno {aluno1.getNome()} foi removido do curso de {curso1.getNome()}.")
    else:
        print(f"O aluno {aluno1.getNome()} não está no curso de {curso1.getNome()}.")
