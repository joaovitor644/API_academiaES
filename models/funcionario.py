from BD.bd import engine
from dataclasses import dataclass
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

@dataclass
class Funcionario:
    nit: int
    nome: str
    data_nascimento: str
    cpf: str
    email: str
    telefone: str
    id_endereco: int
    id_contrato: int


    def  ListarFuncionarios(self, session):
        query = text("""
        SELECT * FROM mydb.funcionario
        """)
        result = session.execute(query)
        funcionarios = result.fetchall()
        return funcionarios
    
    def CadastrarFuncionario(self, session):
        query = text("""
        INSERT INTO mydb.funcionario (nit, nome, data_nascimento, cpf, email, telefone, endereco_id_endereco, contrato_id_contrato) 
        VALUES (:nit, :nome, :data_nascimento, :cpf, :email, :telefone, :endereco_id_endereco, :contrato_id_contrato) 
        """)
        params = {
            "nit": int(self.nit),
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "cpf": self.cpf,
            "email": self.email,
            "telefone": self.telefone,
            "endereco_id_endereco": self.id_endereco,
            "contrato_id_contrato": self.id_contrato
        }
        session.execute(query, params)


    def GetAllFuncionario(self, session):
        query = text("""
                SELECT 
                    f.*,
                    u.id_usuario, u.username, u.is_admin,
                    a.cargo AS cargo_administrador,
                    i.grau_academico AS grau_instrutor,
                    c.id_contrato, c.salario, c.data_contratacao, c.data_final,
                    e.logradouro, e.cep, e.rua, e.num_casa, e.bairro, e.cidade
                FROM mydb.funcionario f
                LEFT JOIN mydb.usuario u ON f.NIT = u.funcionario_NIT
                LEFT JOIN mydb.administrador a ON f.NIT = a.funcionario_NIT
                LEFT JOIN mydb.instrutor i ON f.NIT = i.funcionario_NIT
                LEFT JOIN mydb.contrato c ON f.NIT = c.funcionario_NIT
                LEFT JOIN mydb.endereco e ON f.endereco_id_endereco = e.id_endereco
                WHERE f.NIT = :nit
        """)
        params = {
            "nit": str(self.nit)
        }
        result = session.execute(query, params)
        funcionario = result.fetchone()
        return funcionario

       