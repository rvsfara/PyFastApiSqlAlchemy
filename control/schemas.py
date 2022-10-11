# Esta camada irá conter as Classes que irao representar os dados que serão
# recebidos e retornados no corpo de uma requisição ou resposta HTTP

# Pydantic é uma biblioteca que vem junto com o FatAPI
# tem como objetivo promover uma validação através de dados pelo Type Hints do Python
# o FatAPI usa o Pydantic para validação e para realizar a tipage dos dados que 
# são recebidos e retornados nas requisições e respostas HTTP, também usa a tipagem
# para gerar a documentação do projeto
from pydantic import BaseModel

# esta classe ira herdar de BaseModel e nela deve ser definido o que é comum nas 
# classes CursoRequest e CursoResponse e não realizamos duplicação de código
class CursoBase(BaseModel):
    titulo: str
    descricao: str
    carga_horaria: int
    qtd_exercicios: int

# Tudo que esperamos receber no corpo das nossas requisições HTTP
# como não colocamos atributos a mais so tera o que herdou da CursoBase
class CursoRequest(CursoBase):
    #...

# tudo que queremos retornar do corpo de nossas respostas HTTP, definimos apenas o atributo id
class CursoResponse(CursoBase):
    id: int
    # classe que serve para passarmos configurações adicionais para o Pydantic
    # a opção orm_mode true habilita um método estático from_orm que permite criar uma 
    # instancia do modelo do Pydantic a partir de uma classe de modelo da nossa ORM
    class Config:
        orm_mode = True 
