from dataclasses import dataclass
from sqlalchemy.orm import sessionmaker
from BD.bd import engine
from sqlalchemy.sql import text

@dataclass
class Aluno:
    matricula: int
    nome: str
    data_nascimento: str
    cpf: str
    email: str
    telefone: str
    id_endereco: int
    plano_id: int

    def CadastrarAluno(self, session):
        query = text("""
        INSERT INTO mydb.aluno (matricula, nome, data_nascimento, cpf, email, telefone, endereco_id_endereco, plano_id_plano) 
        VALUES (:matricula, :nome, :data_nascimento, :cpf, :email, :telefone, :endereco_id_endereco, :plano_id) 
        """)
        params = {
            "matricula": int(self.matricula),
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "cpf": self.cpf,
            "email": self.email,
            "telefone": self.telefone,
            "endereco_id_endereco": self.id_endereco,
            "plano_id": int(elf.plano_id)
        }
        session.execute(query, params)
        

    def AtualizarAluno(self):
        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()
            query = """
            UPDATE Aluno SET
            nome = :nome, 
            data_nascimento = :data_nascimento, 
            cpf = :cpf, 
            email = :email, 
            telefone = :telefone 
            WHERE id_aluno = :matricula
            """
            params = {
                "nome": self.nome,
                "data_nascimento": self.data_nascimento,
                "cpf": self.cpf,
                "email": self.email,
                "telefone": self.telefone,
                "matricula": self.matricula
            }
            session.execute(query, params)
            session.commit()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            session.rollback()
            return False
        finally:
            session.close()
            

    def ExcluirAluno(self, matricula):

        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()
            query = "DELETE FROM Aluno WHERE id_aluno = :matricula"
            params = {"matricula": matricula}
            session.execute(query, params)
            session.commit()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            session.rollback()
            return False
        finally:
            session.close()


    def ListarAluno(self):
        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()    
            query = text("""SELECT * FROM mydb.aluno""")
            result = session.execute(query)
            return result.fetchall()
        except Exception as e:
            print(f"Erro: {e}")
            session.rollback()
            return False
        finally:
            session.close()


    def UpdateAluno(self):
        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()
            query = """
            UPDATE Aluno SET
            nome = :nome, 
            data_nascimento = :data_nascimento, 
            cpf = :cpf, 
            email = :email, 
            telefone = :telefone 
            WHERE id_aluno = :matricula
            """
            params = {
                "nome": self.nome,
                "data_nascimento": self.data_nascimento,
                "cpf": self.cpf,
                "email": self.email,
                "telefone": self.telefone,
                "matricula": self.matricula
            }
            session.execute(query, params)
            session.commit()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False
        finally:
            session.close()

    def GetAluno(self, session):
        query = text("SELECT * FROM mydb.aluno WHERE matricula = :matricula")
        params = {"matricula": self.matricula}
        result = session.execute(query, params)
        return result.fetchone()
   

    def GetAulasAluno(self):
        try:
            session = sessionmaker(bind=engine)
            query = text("""
            SELECT a.horario, a.tipo, a.sala, f.nome, f.NIT
            FROM aula a
            JOIN aula_has_aluno aa ON a.id_aula = aa.aula_id_aula
            JOIN aluno al ON al.matricula = aa.aluno_matricula
            JOIN aula_has_funcionario af ON a.id_aula = af.aula_id_aula
            JOIN funcionario f ON f.NIT = af.funcionario_NIT
            WHERE al.matricula = :matricula
            """)
            params = {"matricula": self.matricula}
            result = session.execute(query, params)
            return result.fetchall()
        except Exception as e:
            print(f"Erro: {e}")
            session.rollback()
            return False
        finally:
            session.close()
