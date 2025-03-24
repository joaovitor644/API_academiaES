from BD.bd import engine
from dataclasses import dataclass
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from typing import Optional

@dataclass
class Login:
    username: str
    password: str
    is_adm: Optional[bool] = None


    def Auth(self):
        try:
            sessionLocal = sessionmaker(bind=engine)    
            session = sessionLocal()
            query = text("""SELECT * FROM mydb.usuario WHERE username = :username""")
            params = {
                "username": self.username
            }
            result = session.execute(query, params)
            user = result.fetchone()
            session.commit()
            return user
        except Exception as e:
            return str(e)
        finally:
            session.close()


    def CadastrarUser(self, session):
        
        query = text("""
        INSERT INTO mydb.usuario (username, senha_hash, is_admin)
        VALUES (:username, :password, :is_adm)
        RETURNING id_usuario
        """)
        params = {
            "username": self.username,
            "password": self.password,
            "is_adm": self.is_adm
        }
        result = session.execute(query, params)
        id_usuario = result.fetchone()[0]
        return id_usuario

    
