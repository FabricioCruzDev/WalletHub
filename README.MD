# 💰 WALLETHUB

O **WALLETHUB** é uma solução de gerenciamento financeiro pessoal multiplataforma projetada para consolidar gastos de débito e crédito em um único lugar. O foco do sistema é oferecer uma visão clara do consumo do usuário, categorizando despesas de forma inteligente e fornecendo alertas críticos para a saúde financeira.

## 🏗️ Arquitetura e Filosofia
O projeto adota a filosofia **Client-First**, priorizando a experiência e a disponibilidade do usuário:
* **Local Storage (Client-Side):** Utiliza **SQLite** para persistência imediata de dados nos dispositivos móveis e desktop, garantindo funcionamento offline completo.
* **Sincronização (Server-Side):** Integração assíncrona com **PostgreSQL (via Supabase)** para backup, persistência em nuvem e consistência de dados entre dispositivos.
* **Multiplataforma:** Interface única desenvolvida para rodar em Android, iOS e Desktop (Windows/Linux/macOS) utilizando a mesma base de código.

## 🚀 Funcionalidades Principais
* **Consolidação de Gastos:** Unificação de transações via débito e crédito em uma interface coesa.
* **Gestão de Cartões:** Controle de múltiplos cartões de crédito com limite, data de fechamento e vencimento.
* **Categorização Inteligente:** Registro e organização de despesas com campos de descrição, data e valor.
* **Fluxo de Caixa Real:** Débitos automáticos de contas e registros de crédito com atualização de faturas.
* **Despesas Fixas:** Gerenciamento de contas recorrentes com lembretes de vencimento.
* **Inteligência Financeira:** Geração de estimativas de gastos futuros com base no histórico.

## 🛠️ Stack Tecnológica
* **Linguagem:** Python 3.14.3
* **Framework UI:** [Flet](https://flet.dev/) (Baseado em Flutter)
* **Banco de Dados Local:** SQLite
* **Banco de Dados Remoto & Auth:** Supabase (PostgreSQL)
* **Driver de Conexão:** Psycopg3 (Binary)
* **Gerenciamento de Dependências:** pip

## 📥 Instalação e Configuração

### Pré-requisitos
* Python 3.14.3 instalado.
* Conta ativa no Supabase.

### Instalação de Dependências
```bash
pip install flet psycopg[binary] python-dotenv