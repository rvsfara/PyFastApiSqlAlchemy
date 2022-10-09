# importamos as classes do SQLAlchemy para usar em nosso model
# a Classe Column para definir as colunas da tabela
# as Classes Integer e String os tipos de dados utilizados nas colunas de nossa tabela
from sqlalchemy import Column, Integer, String
# a claase Base é a classe que todas as classes de modelo devem herdar
from database import Base

# classe que representa a tabela Cliente no banco de dados
# o SQLAlchemy irá utilizar esta classe para gerar as tabelas de forma automática
class Cliente(Base):
    # atributo usado pelo SQLAlchemy para informar o nome da tabela
    __tablename__ = "tb_cliente"
    
    # demais colunas da tabela, 
    # lembrando que usamos o recurso de tipagem Type Hints do python
    id: int = Column(Integer, primary_key=True, index=True)
    cpf: str = Column(String(14), nullable=False)
    nome: str = Column(String(100), nullable=False)
    dtNascimento: str = Column(String(10), nullable=False)
    email: str = Column(String(100), nullable=False)
    senha: str = Column(String(100), nullable=False)
