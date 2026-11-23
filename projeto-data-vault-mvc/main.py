from log_auditoria_view import LogAuditoriaView
from view import SuspeitoView
from view_model import SuspeitoViewModel


if __name__ == "__main__":
    vm = SuspeitoViewModel()
    view = SuspeitoView(vm)
    LogAuditoriaView(vm)
    view.iniciar()
