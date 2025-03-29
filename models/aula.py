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
        RETURNING id_aula
        """)
        params_aula = {
            "horario": self.horario,
            "tipo": self.tipo,
            "sala": self.sala
        }
        result = session.execute(query_aula, params_aula)
        self.id_aula = result.fetchone()[0]

    def CadastrarFuncionarioAula(self, funcionario_nit, id_aula, session):
        query = text("""
        INSERT INTO mydb.aula_has_funcionario (aula_id_aula, funcionario_nit)
        VALUES (:id_aula, :funcionario_nit) 
        """)
        params = {
            "id_aula": id_aula,
            "funcionario_nit": funcionario_nit
        }
        session.execute(query, params)

    def ExcluirFuncionarioAula(self, funcionario_nit, session):
        query = text("DELETE FROM mydb.aula_has_funcionario WHERE funcionario_nit = :funcionario_nit")
        params = {"funcionario_nit": funcionario_nit}
        session.execute(query, params)

            

    def ListarAula(self, session):
        query = text("""SELECT * FROM mydb.aula""")
        result = session.execute(query)
        return result.fetchall()
        



    def GetAllAula(self, id_aula, session):
        query = text("""
        SELECT a.* FROM mydb.aula a
        COALESCE(array_agg(DISTINCT f.funcionario_NIT), '{}') AS ids_funcionario
        LEFT JOIN mydb.aula_has_funcionario ahf ON a.id_aula = ahf.aula_id_aula
        LEFT JOIN mydb.funcionario f ON ahf.funcionario_NIT = f.NIT
        WHERE a.id_aula = :id_aula
        GROUP BY a.id_aula;
        """)
        params = {
            "id_aula": id_aula
        }
        return session.execute(query, params).fetchone()
    


    def AtualizarAula(self, id_aula, session):
        query = text("""
        UPDATE mydb.aula SET
        horario = :horario,
        tipo = :tipo,
        sala = :sala
        WHERE id_aula = :id_aula
        """)
        params = {
            "horario": self.horario,
            "tipo": self.tipo,
            "sala": self.sala,
            "id_aula": id_aula
        }
        session.execute(query, params)

    def ExcluirAula(self, id_aula, session):
        query = text("DELETE FROM mydb.aula WHERE id_aula = :id_aula")
        params = {"id_aula": id_aula}
        session.execute(query, params)