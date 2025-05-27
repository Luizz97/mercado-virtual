import tkinter as tk
from tkinter import ttk, messagebox
from projeto_livre.models.usuario import Usuario
from projeto_livre.models.produto import Produto
from projeto_livre.models.carrinho import Carrinho
from projeto_livre.models.pagamento import CartaoCredito, Boleto, Pix
from projeto_livre.models.pedido import Pedido


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("🛒 Mercado Virtual")
        self.root.geometry("750x800")
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.configurar_estilos()

        self.usuario = None
        self.produtos = Produto.carregar_produtos()
        self.carrinho = None
        self.frame_login()


    def finalizar_compra(self):
        total = self.carrinho.total()

        def confirmar_pagamento(metodo):
            messagebox.showinfo("Método Selecionado", f"Você escolheu: {metodo}")
            
            if metodo == "Cartão de Crédito":
                forma = CartaoCredito()
            elif metodo == "Boleto":
                forma = Boleto()
            elif metodo == "Pix":
                forma = Pix()
            else:
                messagebox.showerror("Erro", "Método inválido.")
                return

            pedido = Pedido(total, forma)
            mensagem_pagamento = pedido.finalizar_pedido()

            messagebox.showinfo("Pagamento", mensagem_pagamento)
            messagebox.showinfo("✅ Sucesso", "Compra realizada com sucesso!")

            self.carrinho.limpar()
            resposta = messagebox.askyesno(
                "Continuar",
                "Deseja fazer outra compra?"
            )
            if resposta:
                self.carrinho = Carrinho.carregar_para_usuario(self.usuario.email, Produto)
                self.frame_produtos()
            else:
                self.frame_login()

        janela = tk.Toplevel(self.root)
        janela.title("🧾 Finalizar Pagamento")
        janela.geometry("360x280")
        janela.resizable(False, False)
        janela.configure(bg="#f1f2f6")

        container = ttk.Frame(janela, padding=20)
        container.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(
            container,
            text="💰 Selecione a forma de pagamento:",
            style='Cabecalho.TLabel',
            justify='center'
        ).pack(pady=(0, 20))

        botoes = [
            ("💳 Cartão de Crédito", "Cartão de Crédito"),
            ("🏦 Boleto", "Boleto"),
            ("⚡ Pix", "Pix")
        ]

        for texto, metodo in botoes:
            botao = ttk.Button(
                container,
                text=texto,
                command=lambda m=metodo: [janela.destroy(), confirmar_pagamento(m)],
                style='Botao.TButton',
                width=25
            )
            botao.pack(pady=6)

    def configurar_estilos(self):
        self.style.configure('Titulo.TLabel', font=('Segoe UI', 20, 'bold'), foreground='#00b894')
        self.style.configure('Cabecalho.TLabel', font=('Segoe UI', 12, 'bold'), foreground='#2d3436')
        self.style.configure('Botao.TButton', font=('Segoe UI', 10, 'bold'), padding=8, background='#0984e3', foreground='white')
        self.style.map('Botao.TButton', background=[('active', '#74b9ff')])

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def criar_topo(self, titulo):
        barra = ttk.Frame(self.root)
        barra.pack(fill='x')
        ttk.Label(barra, text=f"🌐 {titulo}", style='Titulo.TLabel').pack(side='left', padx=20, pady=10)
        if self.usuario:
            ttk.Label(barra, text=f"👤 {self.usuario.nome}", style='Cabecalho.TLabel').pack(side='right', padx=20)

    def frame_login(self):
        self.limpar_tela()
        self.criar_topo("Bem-vindo ao Mercado Virtual")

        container = ttk.Frame(self.root)
        container.place(relx=0.5, rely=0.5, anchor='center')

        ttk.Label(container, text="🔐 Login", style='Titulo.TLabel').pack(pady=20)

        frame_campos = ttk.Frame(container)
        frame_campos.pack(pady=10)

        ttk.Label(frame_campos, text="📧 Email:").grid(row=0, column=0, pady=5, sticky='e')
        self.email_entry = ttk.Entry(frame_campos, width=35)
        self.email_entry.grid(row=0, column=1, pady=5, padx=10)

        ttk.Label(frame_campos, text="🔒 Senha:").grid(row=1, column=0, pady=5, sticky='e')
        self.senha_entry = ttk.Entry(frame_campos, show='*', width=35)
        self.senha_entry.grid(row=1, column=1, pady=5, padx=10)

        botoes = ttk.Frame(container)
        botoes.pack(pady=15)

        ttk.Button(botoes, text="➡️ Entrar", command=self.login, style='Botao.TButton').pack(side='left', padx=10)
        ttk.Button(botoes, text="🆕 Cadastrar", command=self.frame_cadastro, style='Botao.TButton').pack(side='left', padx=10)

    def frame_cadastro(self):
        self.limpar_tela()
        self.criar_topo("Cadastro de Novo Usuário")

        container = ttk.Frame(self.root)
        container.place(relx=0.5, rely=0.5, anchor='center')

        ttk.Label(container, text="📝 Cadastro", style='Titulo.TLabel').pack(pady=20)

        frame_campos = ttk.Frame(container)
        frame_campos.pack(pady=10)

        ttk.Label(frame_campos, text="👤 Nome:").grid(row=0, column=0, pady=5, sticky='e')
        self.nome_entry = ttk.Entry(frame_campos, width=35)
        self.nome_entry.grid(row=0, column=1, pady=5, padx=10)

        ttk.Label(frame_campos, text="📧 Email:").grid(row=1, column=0, pady=5, sticky='e')
        self.email_entry = ttk.Entry(frame_campos, width=35)
        self.email_entry.grid(row=1, column=1, pady=5, padx=10)

        ttk.Label(frame_campos, text="🔒 Senha:").grid(row=2, column=0, pady=5, sticky='e')
        self.senha_entry = ttk.Entry(frame_campos, show='*', width=35)
        self.senha_entry.grid(row=2, column=1, pady=5, padx=10)

        botoes = ttk.Frame(container)
        botoes.pack(pady=15)
        ttk.Button(botoes, text="✅ Cadastrar", command=self.cadastrar, style='Botao.TButton').pack(side='left', padx=10)
        ttk.Button(botoes, text="↩️ Voltar", command=self.frame_login, style='Botao.TButton').pack(side='left', padx=10)

    def frame_produtos(self):
        self.limpar_tela()
        self.criar_topo("Catálogo de Produtos")

        container = ttk.Frame(self.root)
        container.pack(fill='both', expand=True, padx=20, pady=10)

        canvas = tk.Canvas(container, highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Exibição dos produtos
        for p in self.produtos:
            preco = p.calcular_desconto()
            preco_original = f"R$ {p.preco:.2f}".replace('.', ',')
            preco_com_desconto = f"R$ {preco:.2f}".replace('.', ',')

            frame = ttk.Frame(scrollable_frame, padding=15, relief="ridge", style='Produto.TFrame')
            frame.pack(pady=10, padx=10, fill='x')

            # Descrição e preço
            detalhes = f"📦 {p.detalhes()}"
            ttk.Label(frame, text=detalhes, style='Cabecalho.TLabel', justify='left').grid(row=0, column=0, sticky='w')

            if preco < p.preco:
                ttk.Label(frame, text=f"💲 De: {preco_original} → {preco_com_desconto}",
                        foreground='#d63031', font=('Segoe UI', 10, 'bold')).grid(row=1, column=0, sticky='w', pady=(4, 0))
            else:
                ttk.Label(frame, text=f"💰 Preço: {preco_original}",
                        foreground='#2d3436', font=('Segoe UI', 10, 'bold')).grid(row=1, column=0, sticky='w', pady=(4, 0))

            # Botão adicionar
            ttk.Button(
                frame,
                text="➕ Adicionar",
                command=lambda prod=p: self.adicionar_ao_carrinho(prod),
                style='Botao.TButton'
            ).grid(row=0, column=1, rowspan=2, padx=10)

        ttk.Button(
            container,
            text="🛍️ Ver Carrinho",
            command=self.frame_carrinho,
            style='Botao.TButton'
        ).pack(pady=20)

    def frame_carrinho(self):
        self.limpar_tela()
        self.criar_topo("Seu Carrinho")

        container = ttk.Frame(self.root)
        container.pack(fill='both', expand=True, padx=15, pady=10)

        canvas = tk.Canvas(container, highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        total = 0
        for item in self.carrinho.itens:
            frame = ttk.Frame(scrollable_frame)
            frame.pack(pady=5, fill='x')

            ttk.Label(frame, text=f"🧾 {item.nome} - R$ {item.preco:.2f}".replace('.', ','), width=40, anchor='w').pack(side='left', padx=10)
            ttk.Button(frame, text="❌ Remover", command=lambda nome=item.nome: self.remover_do_carrinho(nome), style='Botao.TButton').pack(side='right')
            total += item.preco

        ttk.Label(container, text=f"💳 Total: R$ {total:.2f}".replace('.', ','), style='Cabecalho.TLabel').pack(pady=10)

        botoes = ttk.Frame(container)
        botoes.pack(pady=15)

        ttk.Button(botoes, text="✅ Finalizar Compra", command=self.finalizar_compra, style='Botao.TButton').pack(side='left', padx=10)
        ttk.Button(botoes, text="↩️ Voltar", command=self.frame_produtos, style='Botao.TButton').pack(side='left', padx=10)

    def login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        user = Usuario.autenticar(email, senha)
        if user:
            self.usuario = user
            self.carrinho = Carrinho.carregar_para_usuario(email, Produto)
            self.frame_produtos()
        else:
            messagebox.showerror("Erro", "Credenciais inválidas")

    def cadastrar(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        novo = Usuario(nome, email, senha)
        Usuario.salvar_usuario(novo)
        messagebox.showinfo("Sucesso", "Usuário cadastrado")
        self.frame_login()

    def adicionar_ao_carrinho(self, produto):
        self.carrinho.adicionar_item(produto)
        self.carrinho.salvar()
        messagebox.showinfo("Carrinho", f"{produto.nome} adicionado.")

    def remover_do_carrinho(self, nome_produto):
        sucesso = self.carrinho.remover_item(nome_produto)
        if sucesso:
            messagebox.showinfo("Removido", f"{nome_produto} foi removido do carrinho.")
            self.frame_carrinho()
        else:
            messagebox.showerror("Erro", "Não foi possível remover o item.")
    
