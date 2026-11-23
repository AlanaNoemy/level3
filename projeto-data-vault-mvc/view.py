class SuspeitoView:
    def __init__(self, view_model):
        self.vm = view_model
        self.vm.registrar_observador(self.renderizar)

    def renderizar(self):
        print("\n" + "=" * 55)
        print(
            f"🛰️  PAINEL REATIVO MVVM | Casos: {self.vm.total_casos} | "
            f"Risco Médio: {self.vm.media_periculosidade:.1f}/10"
        )
        print("=" * 55)
        if self.vm.lista_suspeitos:
            for item in self.vm.lista_suspeitos:
                print(f"  • {item}")
        else:
            print("  (Nenhum suspeito registrado)")
        print("-" * 55)
        print(f"[STATUS]: {self.vm.status_sistema}")
        print("=" * 55)

    def iniciar(self):
        self.renderizar()
        while True:
            print("\n1. Novo Registro | 2. Remover por ID | 0. Sair")
            op = input("Comando: ").strip()
            if op == "1":
                nome = input("Nome: ")
                crime = input("Crime: ")
                nivel = input("Periculosidade (1-10): ")
                self.vm.adicionar_suspeito(nome, crime, nivel)
            elif op == "2":
                suspeito_id = input("ID para remover: ")
                self.vm.remover_suspeito(suspeito_id)
            elif op == "0":
                print("Desligando painel...")
                break
            else:
                print("Comando inválido.")
