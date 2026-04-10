import psycopg as ps
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
DATABASE_URL = os.getenv("DATABASE_URL")

#TESTE DA CONEXÃO
def verificar_conexao():
    try:
        with conn.cursor() as cur:
        # Executa um comando simples: pede a versão do Postgres
            cur.execute("SELECT version();")
            version = cur.fetchone()
              
            print("✅ Conexão estabelecida com sucesso!")
            print(f"🐘 Versão do Banco: {version[0]}")
               
            # Opcional: listar as tabelas que criamos antes
            cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
            tabelas = cur.fetchall()
            print(f"📊 Tabelas encontradas: {[t[0] for t in tabelas]}")
            
        print("Conexão com o banco fechada")

    except Exception as e:
        print("❌ Falha na conexão.")
        print(f"Erro detalhado: {e}")


def create_table_user():
    try:
        with conn.cursor() as cur:
            query = """
                CREATE TABLE IF NOT EXISTS tb_user
                (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    create_at TIMESTAMP DEFAULT NOW(),
                    updated_at TIMESTAMP DEFAULT NOW(),
                    synced BOOLEAN DEFAULT false,
                    is_deleted BOOLEAN DEFAULT false
                )
                """
            cur.execute(query)
        print('Tabela criada com sucesso')
    except Exception as e:
        print("Erro", e)
    finally:
        print("Fechando a conexão")
        conn.close()


if __name__ == "__main__":
    with ps.connect(DATABASE_URL) as conn:
        verificar_conexao()
        create_table_user()