from src.connections.DatabaseConnection import connection
from src.models.Topico import Topico


def atualizar(topico: Topico) -> None:
    with connection:
        connection.execute(
            "UPDATE topicos SET nome = ?, descricao = ?, supertopico_id = ? WHERE id = ?",
            (topico.nome, topico.descricao, topico.supertopico_id, topico.id),
        )
        connection.commit()


def excluir(id: int) -> None:
    with connection:
        connection.execute("DELETE FROM topicos WHERE id = ?", (id,))
        connection.commit()


def inserir(topico: Topico) -> None:
    with connection:
        connection.execute(
            "INSERT INTO topicos (nome, descricao, supertopico_id) VALUES (?, ?, ?)",
            (topico.nome, topico.descricao, topico.supertopico_id),
        )
        connection.commit()


def listar_por_supertopico(supertopico_id: int) -> list[Topico]:
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM topicos WHERE supertopico_id = ?", (supertopico_id,)
        )
        return list(
            map(lambda row: Topico(row[1], row[2], row[3], row[0]), cursor.fetchall())
        )


def procurar(id: int) -> Topico | None:
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM topicos WHERE id = ?", (id,))
        result = cursor.fetchone()
        if not result:
            return None
        return Topico(result[1], result[2], result[3], result[0])


def tracar_caminho(id: int) -> list[dict]:
    with connection:
        cursor = connection.cursor()
        query = """
            WITH RECURSIVE caminho AS (
                SELECT id, nome, supertopico_id
                FROM topicos
                WHERE id = ?
                UNION ALL
                SELECT t.id, t.nome, t.supertopico_id
                FROM topicos t
                INNER JOIN caminho c ON t.id = c.supertopico_id
            )
            SELECT id, nome, supertopico_id FROM caminho
            ORDER BY id ASC
        """
        cursor.execute(query, [id])
        return list(map(lambda row: {"id": row[0], "nome": row[1]}, cursor.fetchall()))
