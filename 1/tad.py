''''
Quando falamos em Tipo abstrato de DADOS (TAD) temos que entender que a ideia central é ENCAPSULAR (esconder) de quem usa um determinado tipo a sua implementação, ou seja, sua forma concreta. Nós podemos criar tipos para representar por exemplo uma pessoa e um cliente dete tipo usará somente a forma abstrata, inclusive, se você quiser trocar uma implementação posteriormente fica mais fácil e transparente para quem usa aquele determinado tipo ou estrutura.

Sendo assim, implemente utilizando C uma TAD Pessoa, definindo o tipo, seus atributos são nome e data_de_nascimento, seus métodos são:

cria_pessoa #que recebe nome, data_de_nascimento

calcula_idade #que recebe uma pessoa como parâmetro e devolve um inteiro com a idade dela

inverte_nome #que recebe uma pessoa e retorna uma string com o nome dela invertido, ex: Heineck, Tiago

Crie a TAD, a implementação e um arquivo com método main que use a TAD Pessoa.

Envio o link do GitHub no campo de resolução e alguns prints de sua tela com o resultado da compilação e o resultado do código executado!'''
class Data_de_nascimento:
  def __init__(self, dia, mes, ano):
    self.dia = dia
    self.mes = mes
    self.ano = ano

class Pessoa:
  def __init__(self, nome, data):
    self.nome = nome 
    self.data_de_nascimento = data

  def calcula_idade(self, Pessoa):
    return (2020 - Pessoa.data_de_nascimento.ano)
  def inverte_nome(self, Pessoa):
    nomeCompleto = Pessoa.nome.split(" ")
    return (nomeCompleto[::-1]) 

