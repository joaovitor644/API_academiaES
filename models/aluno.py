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
            "plano_id": int(self.plano_id)
        }
        session.execute(query, params)
        
    def CadastrarAlunoAula(self, id_aula, session):
        query = text("""
        INSERT INTO mydb.aula_has_aluno (aula_id_aula, aluno_matricula) 
        VALUES (:id_aula, :matricula) 
        """)
        params = {
            "id_aula": id_aula,
            "matricula": self.matricula
        }
        session.execute(query, params)



    def AtualizarAluno(self, session):
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


    def ListarAluno(self, session):    
            query = text("""SELECT * FROM mydb.aluno""")
            result = session.execute(query)
            return result.fetchall()
        


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

    def GetAllAluno(self, session):
        query = text("""SELECT 
            a.matricula, a.nome, a.data_nascimento, a.cpf, a.email, a.telefone,
            e.logradouro, e.cep, e.rua, e.num_casa, e.bairro, e.cidade,
            p.nome AS nome_plano, p.valor AS valor_plano, p.descricao AS descricao_plano,
            af.id_avaliacao_fisica, af.altura, af.peso, af.observacoes, af.biotipo, af.medidas,
            pe.id_pendencia, pe.data_criacao, pe.data_vencimento, pe.descricao AS pendencia_descricao, pe.status AS pendencia_status,
            t.id_treino, t.objetivo, t.dificuldade
        FROM mydb.aluno a
        LEFT JOIN mydb.endereco e ON a.endereco_id_endereco = e.id_endereco
        LEFT JOIN mydb.plano p ON a.plano_id_plano = p.id_plano
        LEFT JOIN mydb.avaliacao_fisica af ON a.matricula = af.aluno_matricula
        LEFT JOIN mydb.pendencia pe ON a.matricula = pe.aluno_matricula
        LEFT JOIN mydb.treino_has_aluno ta ON a.matricula = ta.aluno_matricula
        LEFT JOIN mydb.treino t ON ta.treino_id_treino = t.id_treino
        WHERE a.matricula = :matricula
        """)
        params = {"matricula": self.matricula}
        result = session.execute(query, params)
        return result.fetchone()
   

    # def GetAulasAluno(self):
    #     try:
    #         session = sessionmaker(bind=engine)
    #         query = text("""
    #         SELECT a.horario, a.tipo, a.sala, f.nome, f.NIT
    #         FROM aula a
    #         JOIN aula_has_aluno aa ON a.id_aula = aa.aula_id_aula
    #         JOIN aluno al ON al.matricula = aa.aluno_matricula
    #         JOIN aula_has_funcionario af ON a.id_aula = af.aula_id_aula
    #         JOIN funcionario f ON f.NIT = af.funcionario_NIT
    #         WHERE al.matricula = :matricula
    #         """)
    #         params = {"matricula": self.matricula}
    #         result = session.execute(query, params)
    #         return result.fetchall()
    #     except Exception as e:
    #         print(f"Erro: {e}")
    #         session.rollback()
    #         return False
    #     finally:
    #         session.close()
