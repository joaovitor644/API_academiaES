from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")
PASSWORD = os.getenv("PASSWORD_BD")
DATABASE_URL = f"postgresql://postgres:{PASSWORD}@{HOST}"
engine = create_engine(DATABASE_URL)

if __name__ == '__main__':
    try:
        with engine.connect() as connection:
            print("Conexão bem-sucedida!")
    except Exception as e:
        print(f"Erro na conexão: {e}")