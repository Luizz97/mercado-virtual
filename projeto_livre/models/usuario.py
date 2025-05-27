import json
import os

USUARIOS_FILE = "database/usuarios.json"

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def to_dict(self):
        return {"nome": self.nome, "email": self.email, "senha": self.senha}

    @staticmethod
    def carregar_usuarios():
        if not os.path.exists(USUARIOS_FILE):
            return []
        with open(USUARIOS_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def salvar_usuario(usuario):
        usuarios = Usuario.carregar_usuarios()
        usuarios.append(usuario.to_dict())
        with open(USUARIOS_FILE, "w") as f:
            json.dump(usuarios, f, indent=4)

    @staticmethod
    def autenticar(email, senha):
        usuarios = Usuario.carregar_usuarios()
        for u in usuarios:
            if u["email"] == email and u["senha"] == senha:
                return Usuario(u["nome"], u["email"], u["senha"])
        return None
