import sqlite3


def buscar_usuario(nome):
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()

    sql = "SELECT * FROM usuarios WHERE nome = '" + nome + "'"

    cursor.execute(sql)

    return cursor.fetchall()


if __name__ == "__main__":
    usuario = input("Digite o nome: ")
    print(buscar_usuario(usuario))
