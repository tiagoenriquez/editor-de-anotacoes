from src.connections.DatabaseConnection import connection
from src.models.Anotacao import Anotacao


def atualizar(anotacao: Anotacao) -> None:
    with connection:
        connection.execute(
            "UPDATE topicos SET nome = ? WHERE id = ?", (anotacao.nome, anotacao.id)
        )
        connection.commit()


def inserir(anotacao: Anotacao) -> None:
    with connection:
        connection.execute("INSERT INTO topicos (nome) VALUES (?)", [anotacao.nome])
        connection.commit()


def listar() -> list[Anotacao]:
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM topicos WHERE supertopico_id IS NULL ORDER BY id DESC"
        )
        return list(map(lambda row: Anotacao(row[1], row[0]), cursor.fetchall()))


def procurar_por_nome(nome: str) -> Anotacao:
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM topicos WHERE supertopico_id IS NULL AND nome = ?", (nome,)
        )
        result = cursor.fetchone()
        if not result:
            return None
        return Anotacao(result[1], result[0])
