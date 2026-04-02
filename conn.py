import psycopg as ps
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to the database
conn_str = ps.connect(DATABASE_URL)

#TESTE DA CONEXÃO
def verificar_conexao():
    try:
        # Tenta estabelecer a conexão
        with conn_str as conn:
            # Cria um cursor para executar comandos
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
            
            conn.close()
            print("Conexão com o banco fechada")

    except Exception as e:
        print("❌ Falha na conexão.")
        print(f"Erro detalhado: {e}")

if __name__ == "__main__":
    verificar_conexao()