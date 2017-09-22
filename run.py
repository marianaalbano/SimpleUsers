from flask import Flask, render_template, request, redirect, url_for
from Model.Model import Users
import json

app = Flask(__name__)

@app.route("/usuarios/")
def usuarios():
    users = json.loads(Users.objects.all().to_json())
    print users
    return render_template('lista.html', users=users)

@app.route("/cadastro/", methods=['GET','POST'])
def cadastro():
    if request.method == 'POST':
        try:
            user = Users()
            user.nome = request.form['nome']
            user.telefone = request.form['telefone']
            user.endereco = request.form['endereco']
            user.save()
            return render_template('cadastro.html', message="Cadastrado com sucesso!")
        except Exception as e:
            return render_template('cadastro.html', message="Falha ao cadastrar usuario: %s" %e)
    else:
        return render_template('cadastro.html')


if __name__ == '__main__':
    app.run(debug=True)