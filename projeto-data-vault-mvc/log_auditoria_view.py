from datetime import datetime
from pathlib import Path
import sys


class LogAuditoriaView:
    def __init__(self, view_model, caminho="auditoria.log"):
        self.vm = view_model
        self.caminho = Path(caminho)
        self.vm.registrar_observador(self.registrar_estado)

    def registrar_estado(self):
        data_hora = datetime.now().astimezone().isoformat(timespec="seconds")
        status = " ".join(self.vm.status_sistema.splitlines())
        linha = (
            f"{data_hora} | Casos: {self.vm.total_casos} | "
            f"Risco médio: {self.vm.media_periculosidade:.1f}/10 | {status}\n"
        )

        try:
            with self.caminho.open("a", encoding="utf-8") as arquivo:
                arquivo.write(linha)
        except OSError as erro:
            print(f"Falha ao gravar a auditoria: {erro}", file=sys.stderr)
