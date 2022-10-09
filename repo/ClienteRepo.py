from sqlalchemy.orm import Session

from models import Cliente


class ClienteRepository:
    # busca todos os Clientes Cadastrados
    @staticmethod
    def find_all(db: Session) -> list[Cliente]:
        return db.query(Cliente).all()
    
    # salva um novo Cliente ou edita um já existente com com o merge
    @staticmethod
    def save(db: Session, cliente: Cliente) -> Cliente:
        if cliente.id:
            db.merge(cliente)
        else:
            db.add(cliente)
        db.commit()
        return cliente
    # busca um Cliente com base no id
    @staticmethod
    def find_by_id(db: Session, id: int) -> Cliente:
        return db.query(Cliente).filter(Cliente.id == id).first()
    # verificar se existe algum Cliente cadastrado com base no ID
    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Cliente).filter(Cliente.id == id).first() is not None
    # excluir um Cliente com base no id
    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        cliente = db.query(Cliente).filter(Cliente.id == id).first()
        if cliente is not None:
            db.delete(cliente)
            db.commit()
