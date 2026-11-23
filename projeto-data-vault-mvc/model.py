import sqlite3


class SuspeitoModel:
    def __init__(self, banco="vault_original.db"):
        self.conexao = sqlite3.connect(banco)
        self.conexao.execute(
            """
            CREATE TABLE IF NOT EXISTS suspeitos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                crime TEXT NOT NULL,
                periculosidade INTEGER NOT NULL
            )
            """
        )
        self.conexao.commit()

    def salvar_suspeito(self, nome, crime, periculosidade):
        nome = nome.strip()
        crime = crime.strip()
        try:
            nivel = int(periculosidade)
        except (TypeError, ValueError):
            raise ValueError("Periculosidade deve ser um número inteiro de 1 a 10.")

        if not nome:
            raise ValueError("Nome é obrigatório.")
        if not crime:
            raise ValueError("Crime é obrigatório.")
        if not 1 <= nivel <= 10:
            raise ValueError("Periculosidade deve estar entre 1 e 10.")

        cursor = self.conexao.execute(
            "INSERT INTO suspeitos (nome, crime, periculosidade) VALUES (?, ?, ?)",
            (nome, crime, nivel),
        )
        self.conexao.commit()
        return cursor.lastrowid

    def listar_todos(self):
        return self.conexao.execute(
            "SELECT id, nome, crime, periculosidade FROM suspeitos ORDER BY id"
        ).fetchall()

    def deletar_suspeito(self, suspeito_id):
        try:
            registro_id = int(suspeito_id)
        except (TypeError, ValueError):
            raise ValueError("ID inválido.")

        cursor = self.conexao.execute("DELETE FROM suspeitos WHERE id = ?", (registro_id,))
        self.conexao.commit()
        return cursor.rowcount > 0

    def fechar(self):
        self.conexao.close()
