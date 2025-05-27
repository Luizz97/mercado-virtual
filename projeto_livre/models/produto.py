import json
import os

PRODUTOS_FILE = "database/produtos.json"

class Produto:
    def __init__(self, codigo, nome, preco, tipo=None):  
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.tipo = tipo  # <- Armazena o tipo se existir

    def to_dict(self):
        return {"codigo": self.codigo, "nome": self.nome, "preco": self.preco}

    @staticmethod
    def inicializar_produtos():
        # Cria o arquivo com produtos padrão se não existir
        if not os.path.exists(PRODUTOS_FILE):
            produtos_padrao = [
                {"codigo": 1, "nome": "Arroz 5kg", "preco": 25.99},
                {"codigo": 2, "nome": "Feijão 1kg", "preco": 7.49},
                {"codigo": 3, "nome": "Macarrão 500g", "preco": 3.99},
                {"codigo": 4, "nome": "Óleo de soja", "preco": 6.89},
                {"codigo": 5, "nome": "Açúcar 1kg", "preco": 4.59},
                {"codigo": 6, "nome": "Farinha de trigo 1kg", "preco": 3.29},
                {"codigo": 7, "nome": "Sal 1kg", "preco": 2.49},
                {"codigo": 8, "nome": "Molho de tomate", "preco": 3.49},
                {"codigo": 9, "nome": "Leite condensado", "preco": 4.99},
                {"codigo": 10, "nome": "Atum enlatado", "preco": 6.79},
                {"codigo": 11, "nome": "Leite integral 1L", "preco": 5.99},
                {"codigo": 12, "nome": "Refrigerante 2L", "preco": 8.99},
                {"codigo": 13, "nome": "Água mineral 500ml", "preco": 2.49},
                {"codigo": 14, "nome": "Suco de laranja 1L", "preco": 6.79},
                {"codigo": 15, "nome": "Biscoito recheado", "preco": 3.99},
                {"codigo": 16, "nome": "Chocolate ao leite", "preco": 4.99},
                {"codigo": 17, "nome": "Barra de cereal", "preco": 2.89},
                {"codigo": 18, "nome": "Pão de forma", "preco": 6.49},
                {"codigo": 19, "nome": "Iogurte 170g", "preco": 2.59},
                {"codigo": 20, "nome": "Achocolatado 200ml", "preco": 1.99},
                {"codigo": 21, "nome": "Sabonete", "preco": 1.99},
                {"codigo": 22, "nome": "Pasta de dente", "preco": 3.49},
                {"codigo": 23, "nome": "Shampoo 200ml", "preco": 9.89},
                {"codigo": 24, "nome": "Condicionador 200ml", "preco": 10.49},
                {"codigo": 25, "nome": "Desodorante", "preco": 7.99},
                {"codigo": 26, "nome": "Papel higiênico (4 unid.)", "preco": 7.99},
                {"codigo": 27, "nome": "Detergente líquido", "preco": 2.89},
                {"codigo": 28, "nome": "Desinfetante 500ml", "preco": 5.59},
                {"codigo": 29, "nome": "Esponja de cozinha", "preco": 1.49},
                {"codigo": 30, "nome": "Sabão em pó 1kg", "preco": 8.79}
            ]
            pasta = os.path.dirname(PRODUTOS_FILE)
            if pasta and not os.path.exists(pasta):
                os.makedirs(pasta)
            with open(PRODUTOS_FILE, "w", encoding="utf-8") as f:
                json.dump(produtos_padrao, f, indent=4)

    @staticmethod
    def carregar_produtos():
        Produto.inicializar_produtos()  
        try:
            with open(PRODUTOS_FILE, "r", encoding="utf-8") as f:
                produtos_json = json.load(f)
                return [Produto(**p) for p in produtos_json]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erro ao carregar produtos: {e}")
            return [Produto(**p) for p in produtos_json]

    @staticmethod
    def buscar_por_codigo(codigo):
        produtos = Produto.carregar_produtos()
        for p in produtos:
            if p.codigo == codigo:
                return p
        return None

    def calcular_desconto(self):
        if self.preco > 5:
            return self.preco * 0.9
        else:
            return self.preco
    def detalhes(self):
        return f"Código: {self.codigo} - Produto: {self.nome}"
