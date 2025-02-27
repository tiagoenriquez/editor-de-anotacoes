from flask import Blueprint, Response, redirect, render_template, request, url_for

from src.models.Topico import Topico
from src.services import TopicoService


topico_blueprint = Blueprint("topico", __name__, url_prefix="/topicos")


@topico_blueprint.get("/cadastro/<int:supertopico_id>")
def cadastrar(supertopico_id: int) -> str:
    return render_template(
        "topicos/cadastro.html", supertopico=TopicoService.procurar(supertopico_id)
    )


@topico_blueprint.get("/edicao/<int:id>")
def editar(id: int) -> str:
    try:
        return render_template("topicos/edicao.html", topico=TopicoService.procurar(id))
    except Exception as exception:
        return render_template("erro.html", erro=exception.args[0])


@topico_blueprint.get("/apresentacao/<int:id>")
def mostrar(id: int) -> str:
    try:
        return render_template(
            "topicos/principal.html",
            topico=TopicoService.procurar(id),
            caminho=TopicoService.tracar_caminho(id),
            topicos=TopicoService.listar_por_supertopico(id),
        )
    except Exception as exception:
        return render_template("erro.html", erro=exception.args[0])


@topico_blueprint.post("/atualizacao/<int:id>")
def atualizar(id: int) -> Response:
    try:
        TopicoService.atualizar(
            Topico(
                request.form.get("nome"),
                request.form.get("descricao"),
                request.form.get("supertopico_id"),
                id,
            )
        )
        return redirect(url_for("topico.mostrar", id=id))
    except Exception as exception:
        return redirect(url_for("erro.exibir", erro=exception.args[0]))


@topico_blueprint.post("/exclusao/<int:id>")
def excluir(id: int) -> Response:
    try:
        TopicoService.excluir(id)
        return redirect(url_for("anotacao.listar"))
    except Exception as exception:
        return redirect(url_for("erro.exibir", erro=exception.args[0]))


@topico_blueprint.post("/insercao")
def inserir() -> Response:
    try:
        supertopico_id = request.form.get("supertopico_id")
        TopicoService.inserir(
            Topico(
                request.form.get("nome"),
                request.form.get("descricao"),
                supertopico_id,
            )
        )
        return redirect(url_for("topico.mostrar", id=supertopico_id))
    except Exception as exception:
        return redirect(url_for("erro.exibir", erro=exception.args[0]))
