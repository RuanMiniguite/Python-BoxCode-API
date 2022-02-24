from flask import Flask, jsonify, request
from db import session, Fisica
from db import Juridica, Projeto
from pprint import pprint

app = Flask(__name__)


@app.route("/inicio", methods=["GET"])
@app.route("/olamundo", methods=["GET"])
def olamundo():
    return "<h1> Ola Mundo </h1>", 201


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
        return "", 200
    elif request.method == "PUT":
        fisica = request.json
        session.query(Fisica).filter(Fisica.cpf == cpf).update(
            {"nome": fisica["nome"], "instEnsino": fisica["instEnsino"]}
        )
        session.commit()
        return "", 200
    elif request.method == "DELETE":
        session.query(Fisica).filter(
            Fisica.cpf == cpf
        ).delete()
        session.commit()
        return "", 200

app.run(host="0.0.0.0", port=8080)