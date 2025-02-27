class Topico:
    def __init__(
        self,
        nome: str,
        descricao: str,
        supertopico_id: int,
        id: int | None = None,
    ) -> None:
        self.nome = nome
        self.descricao = descricao
        self.supertopico_id = supertopico_id
        self.id = id
