from src.models.Topico import Topico
from src.models.Anotacao import Anotacao
from src.repositories import TopicoRepository
from src.services import AnotacaoService


def atualizar(topico: Topico) -> None:
    if topico.supertopico_id == "None":
        AnotacaoService.atualizar(Anotacao(topico.nome, topico.id))
    TopicoRepository.atualizar(topico)


def excluir(id: int) -> None:
    TopicoRepository.excluir(id)


def inserir(topico: Topico) -> None:
    TopicoRepository.inserir(topico)


def listar_por_supertopico(supertopico_id: int) -> list[Topico]:
    return TopicoRepository.listar_por_supertopico(supertopico_id)


def procurar(id: int) -> Topico:
    topico = TopicoRepository.procurar(id)
    if not topico:
        raise Exception("Não possível encontrar o tópico")
    return topico


def tracar_caminho(id: int) -> list[dict]:
    return TopicoRepository.tracar_caminho(id)
