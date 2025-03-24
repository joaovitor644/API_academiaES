from dataclasses import dataclass
from sqlalchemy.orm import sessionmaker
from BD.bd import engine
from sqlalchemy.sql import text

@dataclass
class Visitante:
    nome: str
    data_visita: str
    telefone: str
    qunt_visitas: int
    id_endereco: int

    def CadastrarVisitante(self):
        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()
            query = text("""
            INSERT INTO mydb.visitantes (nome, data_visita, telefone, qunt_visitas, endereco_id_endereco) 
            VALUES (:nome, :data_visita, :telefone, :qunt_visitas, :endereco_id_endereco) 
            """)
            params = {
                "nome": self.nome,
                "data_visita": self.data_visita,
                "telefone": self.telefone,
                "qunt_visitas": self.qunt_visitas,
                "endereco_id_endereco": self.id_endereco,
            }
            session.execute(query, params)
            session.commit()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False
        finally:
            session.close()

    def AtualizarVisitante(self, id_visitante):
        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()
            query = text("""
            UPDATE mydb.visitantes SET
            nome = :nome,
            data_visita = :data_visita,
            telefone = :telefone,
            qunt_visitas = :qunt_visitas
            WHERE id_visitantes = :id_visitantes
            """)
            params = {
                "nome": self.nome,
                "data_visita": self.data_visita,
                "telefone": self.telefone,
                "qunt_visitas": self.qunt_visitas,
                "id_visitantes": id_visitante
            }
            session.execute(query, params)
            session.commit()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False
        finally:
            session.close()
            

    def RemoverVisitante(self, id_visitante):

        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()
            query = text("DELETE FROM mydb.visitantes WHERE id_visitantes = :id_visitantes")
            params = {"id_visitantes": id_visitante}
            session.execute(query, params)
            session.commit()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False
        finally:
            session.close()

    def GetVisitante(self, id_visitante):
        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()
            query = text("SELECT * FROM mydb.visitantes WHERE id_visitantes = :id_visitantes")
            params = {"id_visitantes": id_visitante}
            result = session.execute(query, params)
            return result.fetchall()
        except Exception as e:
            print(f"Erro: {e}")
            return False
        finally:
            session.close()
            
    def ListarVisitantes(self):
        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()    
            query = text("""SELECT * FROM mydb.visitantes""")
            result = session.execute(query)
            return result.fetchall()
        except Exception as e:
            print(f"Erro: {e}")
            return False
        finally:
            session.close()

