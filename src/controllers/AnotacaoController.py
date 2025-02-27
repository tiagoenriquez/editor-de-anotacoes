from flask import (
    Blueprint,
    Response,
    redirect,
    render_template,
    request,
    url_for,
)

from src.models.Anotacao import Anotacao
from src.services import AnotacaoService


anotacao_blueprint = Blueprint("anotacao", __name__, url_prefix="/anotacoes")


@anotacao_blueprint.get("/cadastro")
def cadastrar() -> str:
    return render_template("anotacoes/cadastro.html")


@anotacao_blueprint.get("/lista")
def listar() -> str | Response:
    anotacoes = AnotacaoService.listar()
    if anotacoes:
        return render_template("anotacoes/lista.html", anotacoes=anotacoes)
    return redirect(url_for("anotacao.cadastrar"))


@anotacao_blueprint.post("/insercao")
def inserir() -> Response:
    try:
        AnotacaoService.inserir(Anotacao(request.form.get("nome")))
        return redirect(url_for("anotacao.listar"))
    except Exception as exception:
        return redirect(url_for("erro.exibir", erro=exception.args[0]))
