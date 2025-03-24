from BD.bd import engine
from dataclasses import dataclass
from sqlalchemy.orm import sessionmaker

@dataclass
class Funcionario:
    nit: int
    nome: str
    data_nascimento: str
    cpf: str
    email: str
    telefone: str
    id_endereco: int