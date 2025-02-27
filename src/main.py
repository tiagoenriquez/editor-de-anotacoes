from flask import Flask, redirect, url_for

from src.controllers.AnotacaoController import anotacao_blueprint
from src.controllers.ErroController import erro_blueprint
from src.controllers.TopicoController import topico_blueprint

app = Flask(__name__, template_folder="views/templates", static_folder="views/static")


@app.route("/")
def hello_world():
    return redirect(url_for("anotacao.listar"))


app.register_blueprint(anotacao_blueprint)
app.register_blueprint(erro_blueprint)
app.register_blueprint(topico_blueprint)


if __name__ == "__main__":
    app.run()
