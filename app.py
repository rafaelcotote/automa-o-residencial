#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from automate import inicializaBoard, definePinoComoSaida, escreveParaPorta

inicializaBoard()
definePinoComoSaida(7)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def submit():
    comando=request.form['comando']
    print(comando)

    if(comando == '1ON'):
       escreveParaPorta(7,0) 
    if(comando == '1OFF'):
       escreveParaPorta(7,1)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
