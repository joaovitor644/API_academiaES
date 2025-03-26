from dataclasses import dataclass
from sqlalchemy.sql import text


@dataclass
class Plano:
    nome: str
    valor: float
    descricao: str


    def CadastrarPlano(self,session):
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
        


    def ListarPlano(self, session):
        query = text("""
        SELECT * FROM mydb.plano
        """)
        result = session.execute(query)
        return result.fetchall()
    