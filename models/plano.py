from dataclasses import dataclass
from BD.bd import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text


@dataclass
class Plano:
    nome: str
    valor: float
    descricao: str


    def CadastrarPlano(self):
        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()
            query = text("""
            INSERT INTO mydb.plano (nome, valor, descricao) 
            VALUES (:nome, :valor, :descricao) 
            """)
            params = {
                "nome": self.nome,
                "valor": self.valor,
                "descricao": self.descricao
            }
            session.execute(query, params)
            session.commit()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False
        finally:
            session.close()


    def ListarPlano(self):
        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()
            query = text("""
            SELECT * FROM mydb.plano
            """)
            result = session.execute(query)
            return result.fetchall()
        except Exception as e:
            print(f"Erro: {e}")
            return False
        finally:
            session.close()