from dataclasses import dataclass
from models.funcionario import Funcionario
from sqlalchemy.sql import text

@dataclass
class Adm():
    nit: int
    cargo: str

    def CadastrarAdm(self, session):
        query_administrador = text("""
        INSERT INTO mydb.administrador (funcionario_NIT, cargo)
        VALUES (:funcionario_NIT, :cargo)
        """)
        params_administrador = {
            "funcionario_NIT": self.nit,
            "cargo": self.cargo
        }
        session.execute(query_administrador, params_administrador)

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