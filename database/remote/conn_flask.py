import os
from flask import Flask
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

conn: Client = create_client(
    os.environ.get("DATABASE_URL_FLASK"),
    os.environ.get("DATABASE_KEY")
)


#TESTE DA CONEXÃO
@app.route('/')
def index():
    response = conn.table('tb_user').select("*").execute()
    users = response.data

    html = '<h1>Users</h1><ul>'
    for user in users:
        html += f'<li>{user["name"]} {user["last_name"]}</li>'
    html += '</ul>'

    return html

if __name__ == '__main__':
    app.run(debug=True)



