from dataclasses import dataclass
from sqlalchemy.sql import text

@dataclass
class Treino:
    objetivo: str
    descricao: str
    id_aluno: int

    def CadastrarTreino(self, session):
        query = text("""
        INSERT INTO mydb.treino (objetivo, descricao) 
        VALUES (:objetivo, :descricao) 
        """)
        params = {
            "objetivo": self.objetivo,
            "descricao": self.descricao,
            "id_aluno": self.id_aluno
        }
        session.execute(query, params)