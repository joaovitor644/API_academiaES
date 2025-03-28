from dataclasses import dataclass
from sqlalchemy.sql import text

@dataclass
class Contrato:
    salario: float
    data_contratacao: str
    data_final: str


    def CadastrarContrato(self, session):
        query = text("""INSERT INTO mydb.contrato (salario, data_contratacao, data_final)
        VALUES (:salario, :data_contratacao, :data_final)
        RETURNING id_contrato""")
        
        params = {
            "salario": self.salario,
            "data_contratacao": self.data_contratacao,
            "data_final": self.data_final
        }
        result = session.execute(query, params)
        id_contrato = result.fetchone()[0]
        return id_contrato
