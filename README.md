# Editor de Anotações

Esta aplicação tem a pretensão de ajudar quem pretende estudar a realizar suas anotações. Tem as seguintes funcionalidades:

<li>Cadastrar anotação</li>
<li>Listar anotações em um seletor</li>
<li>Visualizar tópicos de anotações e subtópicos de tópicos</li>
<li>Cadastrar tópicos</li>
<li>Atualizar tópicos e anotações</li>
<li>Excluir tópicos e anotações</li>
<br>
Nesta aplicação, anotações são espécies especiais de tópicos, porque não possuem descrição nem tópico hierarquicamente superior.
<br><br>
Esta aplicação foi desenvolvida em Python, com o framework Flask e a visualização foi desenvolvida com o template engine Jinja. Por enquanto, para iniciar esta aplicação, é preciso rodar alguns comando em um terminal ou CMD:

<br>
<li>Para baixar a aplicação</li>

```
git clone https://github.com/tiagoenriquez/editor-de-anotacoes.git
```

<br>
<li>Para entrar na aplicação</li>

```
cd editor-de-anotações
```

<br>

<li>Para criar o ambiente virtual do Python</li>

```
python -m venv venv
```

<br>
Para entrar no ambiente virtual (no Linux)

```
source venv/bin/activate
```

<br>
Para entrar no ambiente virtual (no Windows)

```
venv/Scripts/activate
```

<br>
<li>Para baixar as dependências do projeto</li>

```
pip install -r requirements.txt
```

<br>
<li>Para iniciar o banco de dados</li>

```
python -m src.create_database
```

<br>
<li>Para iniciar a aplicação</li>

```
python -m src.main
```
