definition = """
CREATE TABLE IF NOT EXISTS topicos (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR (31),
    descricao TEXT,
    supertopico_id INTEGER,
    FOREIGN KEY(supertopico_id) REFERENCES topicos(id) ON DELETE CASCADE
)
"""
