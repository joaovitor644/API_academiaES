from BD.bd import engine
from dataclasses import dataclass
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

@dataclass
class Aula:
    horario: str
    tipo: str
    sala: str
    id_funcionario: int
    id_aluno: int

    def CadastrarAula(self):
        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()
            
            # Inserir na tabela aula
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
            id_aula = result.fetchone()[0]

            # Inserir na tabela de junção aula_has_funcionario
            query_funcionario = text("""
            INSERT INTO mydb.aula_has_funcionario (aula_id_aula, funcionario_NIT)
            VALUES (:aula_id_aula, :funcionario_NIT)
            """)
            params_funcionario = {
                "aula_id_aula": id_aula,
                "funcionario_NIT": self.id_funcionario
            }
            session.execute(query_funcionario, params_funcionario)

            # Inserir na tabela de junção aula_has_aluno
            query_aluno = text("""
            INSERT INTO mydb.aula_has_aluno (aula_id_aula, aluno_matricula)
            VALUES (:aula_id_aula, :aluno_matricula)
            """)
            params_aluno = {
                "aula_id_aula": id_aula,
                "aluno_matricula": self.id_aluno
            }
            session.execute(query_aluno, params_aluno)

            session.commit()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            session.rollback()
            return False
        finally:
            session.close()



    def ListarAula(self):
        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()
            query = text("""SELECT * FROM mydb.aula""")
            result = session.execute(query)
            return result.fetchall()
        except Exception as e:
            print(f"Erro: {e}")
            return False
        finally:
            session.close()



if __name__ == "__main__":
    aula = Aula("14:20", "Musculação", "Sala 1", 123456789, 123456)
    result = aula.CadastrarAula()
    print(result)