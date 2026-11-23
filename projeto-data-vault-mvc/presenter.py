from model import SuspeitoModel


class SuspeitoPresenter:
    def __init__(self, view=None, model=None):
        self.view = view
        self.model = model if model is not None else SuspeitoModel()

    def ao_solicitar_cadastro(self, nome, crime, nivel):
        try:
            self.model.salvar_suspeito(nome, crime, nivel)
            if self.view:
                self.view.exibir_sucesso("Suspeito cadastrado.")
        except ValueError as erro:
            if self.view:
                self.view.exibir_erro(str(erro))

    def ao_solicitar_listagem(self):
        dados = self.model.listar_todos()
        linhas = [
            f"ID #{item_id:02d} | {nome} | Crime: {crime} | Perigo: {nivel}/10"
            for item_id, nome, crime, nivel in dados
        ]
        if self.view:
            self.view.mostrar_relatorio(linhas, len(dados))

    def ao_solicitar_remocao(self, suspeito_id):
        try:
            removido = self.model.deletar_suspeito(suspeito_id)
            if self.view:
                if removido:
                    self.view.exibir_sucesso("Registro removido.")
                else:
                    self.view.exibir_erro("ID não encontrado.")
        except ValueError as erro:
            if self.view:
                self.view.exibir_erro(str(erro))
