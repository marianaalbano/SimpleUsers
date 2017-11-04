from flask import Flask, render_template, request, redirect, url_for
from Model.Model import Users, db, app
import json
from blueprints.Usuarios import usuarios

app.register_blueprint(usuarios)

if __name__ == '__main__':
    app.run(debug=True)