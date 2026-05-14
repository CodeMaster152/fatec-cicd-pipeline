import sqlite3


def busca_usuario(nome):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    query = f"SELECT * FROM usuarios WHERE nome = '{nome}'"

    cursor.execute(query)

    return cursor.fetchall()


def soma(a, b):
    return a + b


if __name__ == "__main__":
    resultado = soma(2, 3)
    print(f"Resultado: {resultado}")
