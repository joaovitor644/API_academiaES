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

    def CadastrarVisitante(self, session):
        query = text("""
        INSERT INTO mydb.visitantes (nome, data_visita, telefone, qunt_visitas) 
        VALUES (:nome, :data_visita, :telefone, :qunt_visitas) 
        """)
        params = {
            "nome": self.nome,
            "data_visita": self.data_visita,
            "telefone": self.telefone,
            "qunt_visitas": self.qunt_visitas,
        }
        session.execute(query, params)

    def AtualizarVisitante(self, id_visitante, session):
        query = text("""
        UPDATE mydb.visitantes SET
        nome = :nome,
        data_visita = :data_visita,
        telefone = :telefone,
        qunt_visitas = :qunt_visitas
        WHERE id_visitantes = :id_visitantes
        RETURNING id_visitantes
        """)
        params = {
            "nome": self.nome,
            "data_visita": self.data_visita,
            "telefone": self.telefone,
            "qunt_visitas": self.qunt_visitas,
            "id_visitantes": id_visitante
        }
        result = session.execute(query, params)
        id = result.fetchone()
        return id
        
    #Errado
    def RemoverVisitante(self, id_visitante, session):
        query = text("DELETE FROM mydb.visitantes WHERE id_visitantes = :id_visitantes")
        params = {"id_visitantes": id_visitante}
        result = session.execute(query, params)
        return result.rowcount

    def GetVisitante(self, id_visitante, session):
        query = text("SELECT * FROM mydb.visitantes WHERE id_visitantes = :id_visitantes")
        params = {"id_visitantes": id_visitante}
        result = session.execute(query, params)
        return result.fetchone()
            
    def ListarVisitantes(self, session):
        query = text("""SELECT * FROM mydb.visitantes""")
        result = session.execute(query)
        return result.fetchall()

