# Operação Data Vault — Level 3 (MVVM reativo)

Aplicação de terminal em Python com SQLite. Execute `python main.py` nesta pasta. O aplicativo usa `vault_original.db` na pasta de execução e reaproveita os registros existentes nesse arquivo.

- `model.py` cuida da persistência e da validação.
- `view_model.py` mantém o estado observável, calcula os indicadores e notifica os observadores.
- `view.py` recebe comandos e redesenha o painel após cada notificação.
- `log_auditoria_view.py` se inscreve no mesmo ViewModel e acrescenta uma linha a `auditoria.log` a cada notificação.
- `main.py` conecta o ViewModel às duas Views e inicia o painel.

Cadastre seis suspeitos para observar o alerta e a média de periculosidade. Ao remover um dos seis, o painel recalcula a média e o alerta deixa de ser exibido. A View de auditoria registra os indicadores e a mensagem de estado em um arquivo local. O Git ignora esse arquivo.

```bash
cd projeto-data-vault-mvc
python main.py
```
