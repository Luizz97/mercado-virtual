
from projeto_livre.models.pagamento import FormaPagamento

class Pedido:
    def __init__(self, valor_total: float, forma_pagamento: FormaPagamento):
        self.valor_total = valor_total
        self.forma_pagamento = forma_pagamento  # Composição forte

    def finalizar_pedido(self):
        return self.forma_pagamento.pagar(self.valor_total)
        self.forma_pagamento.pagar(self.valor_total)
