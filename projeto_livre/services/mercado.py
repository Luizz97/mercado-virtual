from models.produto import Produto
from models.carrinho import Carrinho

class Mercado:
    def __init__(self, usuario):
        self.usuario = usuario
        self.produtos = Produto.carregar_produtos()
        self.carrinho = Carrinho.carregar_para_usuario(usuario.email, Produto)

    def menu(self):
        while True:
            print("\n=== MENU DO MERCADO ===")
            print("1. Ver produtos")
            print("2. Adicionar produto ao carrinho")
            print("3. Ver carrinho")
            print("4. Finalizar compra")
            print("5. Sair")

            opcao = input("Escolha: ")

            if opcao == "1":
                for p in self.produtos:
                    print(f"[{p.codigo}] {p.nome} - R$ {p.preco:.2f}")
            elif opcao == "2":
                try:
                    codigo = int(input("Digite o código do produto: "))
                    produto = Produto.buscar_por_codigo(codigo)
                    if produto:
                        self.carrinho.adicionar_item(produto)
                        self.carrinho.salvar()
                        print(f"{produto.nome} adicionado.")
                    else:
                        print("Produto não encontrado.")
                except ValueError:
                    print("Código inválido.")
            elif opcao == "3":
                self.carrinho.listar_itens()
            elif opcao == "4":
                self.carrinho.listar_itens()
                confirm = input("Deseja finalizar a compra? (s/n): ")
                if confirm.lower() == "s":
                    print("Compra finalizada!")
                    self.carrinho.limpar()
            elif opcao == "5":
                print("Saindo do mercado.")
                break
            else:
                print("Opção inválida.")
