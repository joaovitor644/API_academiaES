from dataclasses import dataclass
from sqlalchemy.sql import text

@dataclass
class Aula:
    horario: str
    tipo: str
    sala: str
    

    def CadastrarAula(self, session):
        query_aula = text("""
        INSERT INTO mydb.aula (horario, tipo, sala)
        VALUES (:horario, :tipo, :sala)
        """)
        params_aula = {
            "horario": self.horario,
            "tipo": self.tipo,
            "sala": self.sala
        }
        session.execute(query_aula, params_aula)
            

    def ListarAula(self, session):
        query = text("""SELECT * FROM mydb.aula""")
        result = session.execute(query)
        return result.fetchall()
        



if __name__ == "__main__":
    aula = Aula("14:20", "Musculação", "Sala 1", 123456789, 123456)
    result = aula.CadastrarAula()
    print(result)