from dataclasses import dataclass
from sqlalchemy.orm import sessionmaker
from BD.bd import engine
from sqlalchemy.sql import text

@dataclass
class Aparelho:
    nome: str
    quantidade: int
    disponibilidade: str

    def CadastrarAparelho(self):
        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()
            query = text("""
            INSERT INTO mydb.aparelho (nome, quantidade, disponibilidade) 
            VALUES (:nome, :quantidade, :disponibilidade) 
            """)
            params = {
                "nome": self.nome,
                "quantidade": self.quantidade,
                "disponibilidade": self.disponibilidade
            }
            session.execute(query, params)
            session.commit()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False
        finally:
            session.close()

    def AtualizarAparelho(self, id_aparelho):
        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()
            query = text("""
            UPDATE mydb.aparelho SET
            nome = :nome,
            quantidade = :quantidade, 
            disponibilidade = :disponibilidade
            WHERE id_aparelho = :id_aparelho
            """)
            params = {
                "nome": self.nome,
                "quantidade": self.quantidade,
                "disponibilidade": self.disponibilidade,
                "id_aparelho": id_aparelho
            }
            session.execute(query, params)
            session.commit()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False
        finally:
            session.close()
            

    def RemoverAparelho(self, id_aparelho):
        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()
            query = text("DELETE FROM mydb.aparelho WHERE id_aparelho = :id_aparelho")
            params = {"id_aparelho": id_aparelho}
            session.execute(query, params)
            session.commit()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False
        finally:
            session.close()

    def GetAparelho(self, id_aparelho):
        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()
            query = text("SELECT * FROM mydb.aparelho WHERE id_aparelho = :id_aparelho")
            params = {"id_aparelho": id_aparelho}
            result = session.execute(query, params)
            return result.fetchall()
        except Exception as e:
            print(f"Erro: {e}")
            return False
        finally:
            session.close()
            
    def ListarAparelhos(self):
        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()    
            query = text("""SELECT * FROM mydb.aparelho""")
            result = session.execute(query)
            return result.fetchall()
        except Exception as e:
            print(f"Erro: {e}")
            return False
        finally:
            session.close()

