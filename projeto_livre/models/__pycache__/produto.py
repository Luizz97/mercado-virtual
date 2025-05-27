import json
import os

PRODUTOS_FILE = "database/produtos.json"

class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def to_dict(self):
        return {"codigo": self.codigo, "nome": self.nome, "preco": self.preco}

    @staticmethod
    def carregar_produtos():
        if not os.path.exists(PRODUTOS_FILE):
            # Cadastrar produtos padrão
            produtos = [
                {"codigo": 1, "nome": "Arroz", "preco": 20.0},
                {"codigo": 2, "nome": "Feijão", "preco": 8.5},
                {"codigo": 3, "nome": "Macarrão", "preco": 5.75}
            ]
            with open(PRODUTOS_FILE, "w") as f:
                json.dump(produtos, f, indent=4)
        with open(PRODUTOS_FILE, "r") as f:
            return [Produto(**p) for p in json.load(f)]

    @staticmethod
    def buscar_por_codigo(codigo):
        produtos = Produto.carregar_produtos()
        for p in produtos:
            if p.codigo == codigo:
                return p
        return None


