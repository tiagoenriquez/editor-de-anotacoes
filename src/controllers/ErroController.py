from flask import Blueprint, render_template, request

erro_blueprint = Blueprint("erro", __name__, url_prefix="/erros")


@erro_blueprint.get("/")
def exibir() -> str:
    return render_template(
        "erro.html", erro=request.args.get("erro", "Erro desconhecido")
    )
