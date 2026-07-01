class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2026 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

# p = Pessoa("Fátima", 25)
# print(p.nome, p.idade)

p2 = Pessoa.criar_de_data_nascimento(2001, 6, 5, "Fátima")
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(25))