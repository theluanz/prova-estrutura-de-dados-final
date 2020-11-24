from tad import Pessoa,Data_de_nascimento
data = Data_de_nascimento(30, 1, 2002)
p = Pessoa("AA bb cc", data)
print(p.inverte_nome(p)) # inverte o nome
print(p.calcula_idade(p)) # calcula idade

