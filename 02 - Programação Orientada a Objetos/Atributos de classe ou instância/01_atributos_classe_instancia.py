class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"

    def mostrar_valores(self, *objs):
        for obj in objs:
            print(obj)

aluno_1 = Estudante("Julia", 1)
aluno_2 = Estudante("Maria", 2)
aluno_1.mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Afya"
aluno_3 = Estudante("Fátima", 3)

aluno_1.escola ="Unit"
aluno_1.matricula = 3
aluno_2.mostrar_valores(aluno_1, aluno_2, aluno_3)