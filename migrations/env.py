import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# 1. Importa o Base dos seus modelos
from models.user import Base

target_metadata = Base.metadata

# 2. Carrega as variáveis de ambiente do .env
# Usamos o caminho absoluto para garantir que funcione de qualquer diretório
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Objeto de configuração do Alembic
config = context.config

# Configuração de Logs
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata para suporte ao --autogenerate
target_metadata = Base.metadata

def get_url():
    """Recupera a URL do .env ou levanta erro se não existir."""

    url = os.getenv("DATABASE_URL")
    print(f"DEBUG: A URL carregada foi: {url}")
    if not url:
        raise ValueError("ERRO: A variável DATABASE_URL não foi encontrada no arquivo .env")
    return url

def run_migrations_offline() -> None:
    """Modo Offline: Gera o SQL sem se conectar ao banco."""
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Modo Online: Conecta ao banco e aplica as mudanças."""
    
    # Capturamos a seção de configuração do .ini
    configuration = config.get_section(config.config_ini_section, {})
    
    # CORREÇÃO CRÍTICA: Injetamos a URL do .env dentro do dicionário de configuração
    # que será passado para o engine_from_config
    configuration["sqlalchemy.url"] = get_url()
    
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata,
            render_as_batch=True #permite que o SQLite aceite alterações de colunas que ele normalmente não suportaria (importante para o seu projeto)
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()