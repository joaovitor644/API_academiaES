from sqlalchemy.sql import text
from dataclasses import dataclass


@dataclass
class AvaliacaoFisica:
    altura: float
    peso: float
    observacoes: str
    biotipo: str
    medidas: str
    matricula: int

    def CadastrarAvaliacaoFisica(self, session):
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


    def ListarAvaliacaoFisica(self, session):
        query = text("""
        SELECT * FROM mydb.avaliacao_fisica
        """)
        result = session.execute(query)
        return result.fetchall()
    
    def GetAvaliacaoFisica(self, id_avaliacao_fisica, session):
        query = text("SELECT * FROM mydb.avaliacao_fisica WHERE id_avaliacao_fisica = :id_avaliacao_fisica")
        params = {"id_avaliacao_fisica": id_avaliacao_fisica}
        result = session.execute(query, params)
        return result.fetchone()
    
    def AtualizarAvaliacaoFisica(self, id_avaliacao_fisica, session):
        query = text("""
        UPDATE mydb.avaliacao_fisica SET
        altura = :altura,
        peso = :peso,
        observacoes = :observacoes,
        biotipo = :biotipo,
        medidas = :medidas,
        aluno_matricula = :matricula
        WHERE id_avaliacao_fisica = :id_avaliacao_fisica
        RETURNING id_avaliacao_fisica
        """)
        params = {
            "altura": self.altura,
            "peso": self.peso,
            "observacoes": self.observacoes,
            "biotipo": self.biotipo,
            "medidas": self.medidas,
            "matricula": self.matricula,
            "id_avaliacao_fisica": id_avaliacao_fisica
        }
        result = session.execute(query, params)
        id = result.fetchone()
        return id
    
    def RemoverAvaliacaoFisica(self, id_avaliacao_fisica, session):
        query = text("DELETE FROM mydb.avaliacao_fisica WHERE id_avaliacao_fisica = :id_avaliacao_fisica")
        params = {"id_avaliacao_fisica": id_avaliacao_fisica}
        result = session.execute(query, params)
        return result.rowcount

    
    