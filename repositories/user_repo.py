from database.local_conn import Session
from sqlalchemy import select, Uuid, Text, UUID
from models.user import User

def create_user(user: User):
    with Session() as session:
        session.add(user)
        session.commit()


def get_all_user():
    with Session() as session:
        stm = select(User)
        rows = session.scalars(stm).all()
        return rows
    
def get_user(email:str):
    with Session() as session:
        print(email)
        user = session.query(User).filter_by(email = email).first()
        if user:
            return user.name
        else:
            return 'Usuário não encontrado'

def delete_user(id: Uuid):
    with Session() as session:
        user = session.query(User).filter_by(id = id).first()
        if user:
            session.delete(user)
            session.commit()
            return 'Usuário excluído com sucesso'
        else:
            return 'Usuário não encontrado'