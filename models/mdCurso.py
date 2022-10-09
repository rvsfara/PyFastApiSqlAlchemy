# importamos as classes do SQLAlchemy para usar em nosso model
# a Classe Column para definir as colunas da tabela
# as Classes Integer e String os tipos de dados utilizados nas colunas de nossa tabela
from sqlalchemy import Column, Integer, String
# a claase Base é a classe que todas as classes de modelo devem herdar
from database import Base

# classe que representa a tabela Cliente no banco de dados
# o SQLAlchemy irá utilizar esta classe para gerar as tabelas de forma automática
class Curso(Base):
     # atributo usado pelo SQLAlchemy para informar o nome da tabela
    __tablename__ = "tb_curso"
    
    # demais colunas da tabela, 
    # lembrando que usamos o recurso de tipagem Type Hints do python
    id: int = Column(Integer, primary_key=True, index=True)
    titulo: str = Column(String(100), nullable=False)
    descricao: str = Column(String(255), nullable=False)
    carga_horaria: int = Column(Integer, nullable=False)
    qtd_exercicios: int = Column(Integer, nullable=False)
