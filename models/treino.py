from dataclasses import dataclass
from sqlalchemy.sql import text

@dataclass
class Treino:
    objetivo: str
    descricao: str

    def CadastrarTreino(self, session):
        query = text("""
        INSERT INTO mydb.treino (objetivo, dificuldade) 
        VALUES (:objetivo, :dificuldade) 
        """)
        params = {
            "objetivo": self.objetivo,
            "dificuldade": self.descricao
        }
        session.execute(query, params)

    def ListarTrinos(self, session):
        query = text("""
        SELECT * FROM mydb.treino
        """)
        return session.execute(query).fetchall()