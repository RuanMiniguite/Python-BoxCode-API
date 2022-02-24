from flask import Flask, jsonify, request
from db import session, Fisica
from db import Juridica, Projeto
from pprint import pprint

app = Flask(__name__)


@app.route("/inicio", methods=["GET"])
@app.route("/olamundo", methods=["GET"])
def olamundo():
    return "<h1> Ola Mundo </h1>", 201

#Rotas relacionadas a fisica
@app.route("/fisica", methods=["GET", "POST"])
@app.route("/fisica/<int:cpf>", methods=["GET", "PUT", "DELETE"])
def fisica(cpf = None):
    if request.method == "GET":
        if cpf:
            try:
                fisica = (
                    session.query(Fisica)
                    .filter(Fisica.cpf == cpf)
                    .one()
                )
                return (
                    jsonify({"cpf": fisica.cpf, "nome": fisica.nome}),
                    200,
                )
            except Exception as ex:
                return "", 404
        else:
            lista_fisica = []
            fisica = session.query(Fisica).all()
            for c in fisica:
                lista_fisica.append({"cpf": c.cpf, "nome": c.nome})
            return jsonify(lista_fisica), 200
    elif request.method == "POST":
        fisica = request.json
        session.add(
            Fisica(cpf = fisica["cpf"], nome = fisica["nome"], instEnsino = fisica["instEnsino"], idade = fisica["idade"])
        )
        session.commit()
        return "Pessoa fisica cadastrada com sucesso!", 200
    elif request.method == "PUT":
        fisica = request.json
        session.query(Fisica).filter(Fisica.cpf == cpf).update(
            {"nome": fisica["nome"], "instEnsino": fisica["instEnsino"]}
        )
        session.commit()
        return "Pessoa fisica atualizada com sucesso!", 200
    elif request.method == "DELETE":
        session.query(Fisica).filter(
            Fisica.cpf == cpf
        ).delete()
        session.commit()
        return "Pessoa fisica deletada com sucesso!", 200

#Rotas relacionadas a juridica
@app.route("/juridica", methods=["GET", "POST"])
@app.route("/juridica/<int:cnpj>", methods=["GET", "PUT", "DELETE"])
def juridica(cnpj = None):
    if request.method == "GET":
        if cnpj:
            try:
                juridica = (
                    session.query(Juridica)
                    .filter(Juridica.cnpj == cnpj)
                    .one()
                )
                return (
                    jsonify({"cnpj": juridica.cnpj, "nome": juridica.nome, "segmento": juridica.segmento}),
                    200,
                )
            except Exception as ex:
                return "", 404
        else:
            juridica = []
            juridica = session.query(Juridica).all()
            for c in juridica:
                lista_juridica.append({"cnpj": c.cnpj, "nome": c.nome, "segmento": c.segmento})
            return jsonify(lista_juridica), 200
    elif request.method == "POST":
        juridica = request.json
        session.add(
            Juridica(cnpj = juridica["cnpj"], nome = juridica["nome"], segmento = juridica["segmento"])
        )
        session.commit()
        return "Pessoa juridica cadastrada com sucesso!", 200
    elif request.method == "PUT":
        juridica = request.json
        session.query(Juridica).filter(Juridica.cnpj == cnpj).update(
            {"nome": juridica["nome"], "segmento": juridica["segmento"]}
        )
        session.commit()
        return "Pessoa juridica atualizada com sucesso!", 200
    elif request.method == "DELETE":
        session.query(Juridica).filter(
            Juridica.cnpj == cnpj
        ).delete()
        session.commit()
        return "Pessoa juridica deletada com sucesso!", 200

#Rotas relacionadas a projeto
@app.route("/projeto", methods=["GET", "POST"])
@app.route("/projeto/<int:id>", methods=["GET", "PUT", "DELETE"])
def projeto(id = None):
    if request.method == "GET":
        if id:
            try:
                projeto = (
                    session.query(Projeto)
                    .filter(Projeto.id == id)
                    .one()
                )
                return (
                    jsonify({"id": projeto.id, "nome": projeto.nome, "segmento": projeto.segmento}),
                    200,
                )
            except Exception as ex:
                return "", 404
        else:
            projeto = []
            projeto = session.query(Projeto).all()
            for c in projeto:
                lista_projeto.append({"id": c.id, "nome": c.nome, "segmento": c.segmento})
            return jsonify(lista_projeto), 200
    elif request.method == "POST":
        projeto = request.json
        session.add(
            Projeto(id = projeto["id"], nome = projeto["nome"], segmento = projeto["segmento"])
        )
        session.commit()
        return "Projeto cadastrado com sucesso!", 200
    elif request.method == "PUT":
        projeto = request.json
        session.query(Projeto).filter(Projeto.id == id).update(
            {"nome": projeto["nome"], "segmento": projeto["segmento"]}
        )
        session.commit()
        return "Projeto atualizado com sucesso!", 200
    elif request.method == "DELETE":
        session.query(Projeto).filter(
            Projeto.id == id
        ).delete()
        session.commit()
        return "Projeto deletado com sucesso!", 200

app.run(host="0.0.0.0", port=8080)