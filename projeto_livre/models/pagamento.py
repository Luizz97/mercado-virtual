from abc import ABC, abstractmethod

class FormaPagamento(ABC):
    """Classe base para todas as formas de pagamento."""

    @abstractmethod
    def pagar(self, valor):
        pass


class CartaoCredito(FormaPagamento):
    def pagar(self, valor):
        return f"[Cartão de Crédito] Pagamento de R${valor:.2f} realizado com sucesso."


class Boleto(FormaPagamento):
    def pagar(self, valor):
        return f"[Boleto] Boleto no valor de R${valor:.2f} gerado. Vencimento em 3 dias."


class Pix(FormaPagamento):
    def pagar(self, valor):
        return f"[Pix] Chave Pix gerada. Valor de R${valor:.2f} pronto para pagamento."
