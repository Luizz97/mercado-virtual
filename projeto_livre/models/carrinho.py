import json
import os

CARRINHOS_FILE = "database/carrinhos.json"

class Carrinho:
    def __init__(self, email):
        self.email = email
        self.itens = []

    def adicionar_item(self, produto):
        self.itens.append(produto)
        self.salvar()  # Salva automaticamente após adicionar o produto

    def listar_itens(self):
        if not self.itens:
            print("Carrinho vazio.")
            return
        total = 0
        print("\nSeu carrinho:")
        for p in self.itens:
            print(f"- {p.nome} R$ {p.preco:.2f}")
            total += p.preco
        print(f"Total: R$ {total:.2f}")

    def salvar(self):
        carrinhos = Carrinho.carregar_todos()
        carrinhos[self.email] = [p.to_dict() for p in self.itens]
        with open(CARRINHOS_FILE, "w") as f:
            json.dump(carrinhos, f, indent=4)

    def limpar(self):
        self.itens = []
        self.salvar()

    def remover_item(self, nome_produto):
        for i, p in enumerate(self.itens):
            if p.nome == nome_produto:
                del self.itens[i]
            self.salvar()  # salva alteração
            print(f"Item '{nome_produto}' removido do carrinho.")
            return True
            print(f"Item '{nome_produto}' não encontrado no carrinho.")
            return False

    @staticmethod
    def carregar_todos():
        if not os.path.exists(CARRINHOS_FILE):
            return {}
        with open(CARRINHOS_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def carregar_para_usuario(email, produto_cls):
        carrinhos = Carrinho.carregar_todos()
        itens = carrinhos.get(email, [])
        carrinho = Carrinho(email)
        carrinho.itens = [produto_cls(**p) for p in itens]
        return carrinho
    def total(self):
        return sum(item.preco for item in self.itens)
