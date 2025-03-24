from BD.bd import engine
from dataclasses import dataclass
from sqlalchemy.orm import sessionmaker
from models.funcionario import Funcionario
from sqlalchemy.sql import text

@dataclass
class Adm(Funcionario):
    token: str

    def CadastrarAdm(self):
        try:
            sessionLocal = sessionmaker(bind=engine)
            session = sessionLocal()
            
            # Inserir na tabela funcionario
            query_funcionario = text("""
            INSERT INTO mydb.funcionario (NIT, nome, data_nascimento, cpf, email, telefone, endereco_id_endereco)
            VALUES (:NIT, :nome, :data_nascimento, :cpf, :email, :telefone, :endereco_id_endereco)
            """)
            params_funcionario = {
                "NIT": self.nit,
                "nome": self.nome,
                "data_nascimento": self.data_nascimento,
                "cpf": self.cpf,
                "email": self.email,
                "telefone": self.telefone,
                "endereco_id_endereco": self.id_endereco  
            }
            session.execute(query_funcionario, params_funcionario)
            
            # Inserir na tabela administrador
            query_administrador = text("""
            INSERT INTO mydb.administrador (funcionario_NIT, token)
            VALUES (:funcionario_NIT, :token)
            """)
            params_administrador = {
                "funcionario_NIT": self.nit,
                "token": self.token
            }
            session.execute(query_administrador, params_administrador)
            
            session.commit()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            session.rollback()
            return False
        finally:
            session.close()

if __name__ == "__main__":
    adm = Adm(
        nit=1,
        nome="John Doe",
        data_nascimento="1990-01-01",
        cpf="123.456.789-00",
        email="john.doe@example.com",
        telefone="123456789",
        token="123456"
    )
    print(adm.CadastrarAdm())