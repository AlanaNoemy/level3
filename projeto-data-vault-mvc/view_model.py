from model import SuspeitoModel


class SuspeitoViewModel:
    ALERTA_MAXIMO = "🚨 ALERTA MÁXIMO: Mais de 5 casos ativos na investigação!"

    def __init__(self, model=None):
        self.model = model if model is not None else SuspeitoModel()
        self._observadores = []
        self.lista_suspeitos = []
        self.total_casos = 0
        self.media_periculosidade = 0.0
        self.status_sistema = "Sistema pronto."
        self.sincronizar_estado(notificar=False)

    def registrar_observador(self, callback):
        self._observadores.append(callback)

    def _notificar(self):
        for callback in tuple(self._observadores):
            callback()

    def sincronizar_estado(self, notificar=True):
        dados = self.model.listar_todos()
        self.lista_suspeitos = [
            f"ID #{suspeito_id:02d} | {nome} | Crime: {crime} | Perigo: {nivel}/10"
            for suspeito_id, nome, crime, nivel in dados
        ]
        self.total_casos = len(dados)
        soma = sum(nivel for _, _, _, nivel in dados)
        self.media_periculosidade = soma / self.total_casos if self.total_casos else 0.0

        if self.total_casos > 5:
            self.status_sistema = self.ALERTA_MAXIMO
        elif self.status_sistema == self.ALERTA_MAXIMO:
            self.status_sistema = "Sistema pronto."

        if notificar:
            self._notificar()

    def adicionar_suspeito(self, nome, crime, periculosidade):
        try:
            self.model.salvar_suspeito(nome, crime, periculosidade)
        except ValueError as erro:
            self.status_sistema = f"❌ Erro: {erro}"
            self._notificar()
            return

        self.status_sistema = f"✅ Suspeito '{nome.strip()}' adicionado ao cofre."
        self.sincronizar_estado()

    def remover_suspeito(self, suspeito_id):
        try:
            removido = self.model.deletar_suspeito(suspeito_id)
        except ValueError:
            self.status_sistema = "❌ Erro: ID inválido."
            self._notificar()
            return

        if removido:
            self.status_sistema = f"🗑️ Registro #{suspeito_id} removido."
            self.sincronizar_estado()
        else:
            self.status_sistema = "⚠️ ID não encontrado."
            self._notificar()
