from flask import Blueprint, render_template, request, redirect, url_for
from Model.Model import Users, db, app
import json


usuarios = Blueprint('usuarios', __name__)


@usuarios.route("/usuarios/")
def user():
    users = Users.query.all()
    print users
    return render_template('lista.html', users=users)

@usuarios.route("/cadastro/", methods=['GET','POST'])
def cadastro():
    if request.method == 'POST':
        try:
            user = Users()
            user.nome = request.form['nome']
            user.telefone = request.form['telefone']
            user.endereco = request.form['endereco']
            db.session.add(user)
            db.session.commit()
            return render_template('cadastro.html', message="Cadastrado com sucesso!")
        except Exception as e:
            return render_template('cadastro.html', message="Falha ao cadastrar usuario: %s" %e)
    else:
        return render_template('cadastro.html')