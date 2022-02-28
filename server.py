from flask import Flask, jsonify, request
from db import session, Fisica
from db import Juridica, Projeto
from pprint import pprint
import _thread
import time
import zmq

app = Flask(__name__)

fila_msg = []

def validarUser():
    IP_ADDRESS = "10.0.1.10"
    TOPIC = "test"

    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUB)
    sock.connect(f"tcp://{IP_ADDRESS}:5500")

    print(f"Starting publishing to the topic {TOPIC}...")
    i = 1
    while True:
        if (len(fila_msg) > 0):
            valor = fila_msg.pop(0)
            sock.send_string(f"{valor}", flags=zmq.SNDMORE)
            print(f"{valor}")
        else:
            print("Sem mensagem nova...")
        time.sleep(1)

    sock.close()
    ctx.term()



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
                    jsonify({"cpf": fisica.cpf, "nome": fisica.nome, "idade": fisica.idade, "instEnsino": fisica.instEnsino}),
                    200,
                )
            except Exception as ex:
                return "", 404
        else:
            lista_fisica = []
            fisica = session.query(Fisica).all()
            for c in fisica:
                lista_fisica.append({"id": c.id, "cpf": c.cpf, "nome": c.nome, "idade": c.idade, "instEnsino": c.instEnsino})
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
            {"nome": fisica["nome"], "instEnsino": fisica["instEnsino"], "idade": fisica["idade"]}
        )
        session.commit()
        return "Pessoa fisica atualizada com sucesso!", 200
    elif request.method == "DELETE":
        session.query(Fisica).filter(
            Fisica.cpf == cpf
        ).delete()
        session.commit()
        return "", 201

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
            lista_juridica = []
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
        return "", 201

#Rotas relacionadas a projeto
@app.route("/projeto", methods=["GET", "POST"])
@app.route("/projeto/<string:nome>", methods=["GET", "PUT", "DELETE"])
def projeto(nome = None):
    if request.method == "GET":
        if nome:
            try:
                projeto = (
                    session.query(Projeto)
                    .filter(Projeto.nome == nome)
                    .one()
                )
                return (
                    jsonify({"id": projeto.id, "nome": projeto.nome, "segmento": projeto.segmento, "descricao": projeto.descricao, "cpf": projeto.cpf, "cnpj": projeto.cnpj}),
                    200,
                )
            except Exception as ex:
                return "", 404
        else:
            lista_projeto = []
            projeto = session.query(Projeto).all()
            for c in projeto:
                lista_projeto.append({"id": c.id, "nome": c.nome, "segmento": c.segmento, "descricao": c.descricao, "cpf": c.cpf, "cnpj": c.cnpj})
            return jsonify(lista_projeto), 200
    elif request.method == "POST":
        projeto = request.json
        session.add(
            Projeto(nome = projeto["nome"], segmento = projeto["segmento"], descricao = projeto["descricao"], cpf = projeto["cpf"], cnpj = projeto["cnpj"])
        )
        session.commit()
        return "", 200
    elif request.method == "PUT":
        projeto = request.json
        session.query(Projeto).filter(Projeto.nome == nome).update(
            {"nome": projeto["nome"], "segmento": projeto["segmento"], "descricao": projeto["descricao"]}
        )
        session.commit()
        return "", 200


_thread.start_new_thread(validarUser, ())
app.run(host="10.0.1.10", port=8080)
