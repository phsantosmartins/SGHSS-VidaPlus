from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)

# Configurações
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///vidaPlus.db"
app.config["JWT_SECRET_KEY"] = "segredo"

db = SQLAlchemy(app)
jwt = JWTManager(app)

# ----------------------
# Rota inicial
# ----------------------
@app.route("/")
def home():
    return {"msg": "Sistema VidaPlus ativo"}

# ----------------------
# Login
# ----------------------
@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email")
    senha = request.json.get("senha")

    if email == "admin@vidaplus.com" and senha == "123":
        token = create_access_token(identity=email)
        return {"token": token}

    return {"erro": "Credenciais inválidas"}, 401

# ----------------------
# Cadastro paciente
# ----------------------
@app.route("/pacientes", methods=["POST"])
def cadastrar_paciente():
    dados = request.json
    return {"msg": "Paciente cadastrado", "dados": dados}

# ----------------------
# Executar servidor
# ----------------------
if __name__ == "__main__":
    app.run(debug=True)


import requests

login = requests.post(
    "http://127.0.0.1:5000/login",
    json={
        "email": "admin@vidaplus.com",
        "senha": "123"
    }
)

print(login.json())