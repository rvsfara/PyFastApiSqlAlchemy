//arquivo de configuração do banco de dados
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# String de conexão com o banco de dados
DATABASE_URL = os.environ.get("DATABASE_URL") or "sqlite:///db.sqlite3"

# método que o SQLAlchemy precisa para criar a conexão com o banco de dados
# passamos a URL do banco de dadados e o segundo argumento necessário apenas para o SQLAlchemy
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
# Classe que irá representar a sessão com o banco de dados, 
# criada por intermédio da função sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# clase Base utilizada como modelo para outras classes de nosso banco de dados
Base = declarative_base()

# esta função disponibiliza uma instância da classe SessionLocal 
# para criar as novas sessões com banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
