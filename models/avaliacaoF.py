from sqlalchemy.sql import text
from dataclasses import dataclass

@dataclass
class AvaliacaoF:
    altura: float
    peso: float
    observacoes: str
    biotipo: str
    medidas: str
    matricula: int


    def CadastrarAvaliacaoF(self, session):
        query = text("""
        INSERT INTO mydb.avaliacao_fisica (altura, peso, observacoes, biotipo, medidas, aluno_matricula) 
        VALUES (:altura, :peso, :observacoes, :biotipo, :medidas, :matricula) 
        """)
        params = {
            "altura": self.altura,
            "peso": self.peso,
            "observacoes": self.observacoes,
            "biotipo": self.biotipo,
            "medidas": self.medidas,
            "matricula": self.matricula
        }
        session.execute(query, params)


    def ListarAvaliacaoF(self, session):
        query = text("""
        SELECT * FROM mydb.avaliacao_fisica
        """)
        result = session.execute(query)
        return result.fetchall()