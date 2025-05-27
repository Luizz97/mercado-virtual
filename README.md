# Projeto Livre - E-commerce Simples

[![GitHub](https://img.shields.io/badge/Ver%20no%20GitHub-luizz97%2Fmercado--virtual-blue?logo=github)](https://github.com/luizz97/mercado-virtual)

Este projeto é um sistema simples de e-commerce em Python, com funcionalidades de cadastro de produtos, gerenciamento de usuários, carrinho de compras e pedidos. Os dados são armazenados em arquivos JSON simulando um banco de dados.

---

## 📁 Estrutura do Projeto

```
projeto_livre_definitivo/
├── main/                        # Scripts de execução
│   ├── main.py                 # Executável principal
│   ├── .env                    # Configurações do ambiente
│   └── database/               # Dados exemplo (produtos e usuários)
├── projeto_livre/              # Código fonte da aplicação
│   ├── app.py                 # Início da aplicação
│   ├── models/                # Modelos de domínio (Produto, Pedido, etc)
│   ├── services/              # Lógica de negócio (Mercado, Pagamento)
│   └── database/              # "Banco de dados" JSON
└── README.md                  # Este arquivo
```

---

## 💻 Requisitos

- Python 3.10 ou superior
- Git (para controle de versão)

---

## ▶️ Como Executar

1. **Clone ou baixe o repositório**:

```bash
git clone https://github.com/luizz97/mercado-virtual.git
cd mercado-virtual
```

2. **Execute o sistema**:

```bash
python main/main.py
```

---

## 💡 Funcionalidades

- Cadastro de produtos e usuários
- Listagem de produtos
- Adição de produtos ao carrinho
- Finalização de pedidos
- Simulação de pagamento
- Armazenamento em arquivos `.json`

---

## 🗂️ Estrutura de Dados JSON

Os dados da aplicação ficam nos arquivos da pasta `database/`:

```
database/
├── produtos.json
├── usuarios.json
└── carrinhos.json
```

---

## 📄 Licença

Este projeto está licenciado sob os termos da **MIT License**.

---

Desenvolvido com fins educacionais.
