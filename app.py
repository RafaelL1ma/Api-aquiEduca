from flask import Flask, redirect, request, Response, render_template, url_for
import csv
import pandas as pd
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/lista-usuario', methods=['GET'])
def listagem(usuario):
    return render_template('lista.html', usuario=usuario)


@app.route("/<id>", methods=['GET'])
def listar(id):
    with open('usuarios.csv', 'r', encoding='utf-8') as cad:
        tabela = csv.reader(cad, delimiter=',')
        for linha in tabela:
            if linha[0] == id:
                usuario = {
                    "id": linha[0],
                    "nome": linha[1],
                    "email": linha[2],
                    "endereco": linha[3],
                    "senha": linha[4],
                    "telefone": linha[5]
                }
                return listagem(usuario)

    return 'Usuário não encontrado.'


@app.route('/cadastro-usuario', methods=['GET'])
def cadastro_usuario():
    return render_template('cadastro.html')


@app.route('/cadastro-salvar', methods=['POST'])
def cadastro_salvar():
    user_info = request.json
    with open('usuarios.csv', 'a', newline='') as cad:
        escrever = csv.writer(cad, delimiter=',')
        usuario = [user_info['id'], user_info['nome'], user_info['email'],
                   user_info['endereco'], user_info['senha'], user_info['telefone']]
        escrever.writerow(usuario)
        id = user_info['id']
