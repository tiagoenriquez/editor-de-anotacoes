from src.models.Anotacao import Anotacao
from src.repositories import AnotacaoRepository


def atualizar(anotacao: Anotacao) -> None:
    outra = AnotacaoRepository.procurar_por_nome(anotacao.nome)
    if outra and outra.id != anotacao.id:
        raise Exception("Já existe outra anotação com o mesmo nome.")
    AnotacaoRepository.atualizar(anotacao)


def inserir(anotacao: Anotacao) -> None:
    if AnotacaoRepository.procurar_por_nome(anotacao.nome):
        raise Exception("Não pode haver duas anotações com o mesmo nome.")
    AnotacaoRepository.inserir(anotacao)


def listar() -> list[Anotacao]:
    return AnotacaoRepository.listar()
