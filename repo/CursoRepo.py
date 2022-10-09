from sqlalchemy.orm import Session

from models import Curso


class CursoRepository:
    # busca todos os Cursos Cadastrados
    @staticmethod
    def find_all(db: Session) -> list[Curso]:
        return db.query(Curso).all()
    
    # salva um novo curso ou edita um já existente com com o merge
    @staticmethod
    def save(db: Session, curso: Curso) -> Curso:
        if curso.id:
            db.merge(curso)
        else:
            db.add(curso)
        db.commit()
        return curso
    
    # busca um Curso com base no id
    @staticmethod
    def find_by_id(db: Session, id: int) -> Curso:
        return db.query(Curso).filter(Curso.id == id).first()
    # verificar se existe algum curso cadastrado com base no ID
    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Curso).filter(Curso.id == id).first() is not None
    # excluir um curso com base no id
    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        curso = db.query(Curso).filter(Curso.id == id).first()
        if curso is not None:
            db.delete(curso)
            db.commit()
