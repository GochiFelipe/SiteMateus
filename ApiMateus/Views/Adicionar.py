from flask import render_template,request
from AdminMateus import app


@app.route('/adicionar-foto')
def adicionarFoto():
    tiposPrincipais = ['Casamento', 'Festa', 'Formatura']
    return render_template('Fotos/adicionarFoto.html', titulo='Adicionar Fotos', tiposPrincipais = tiposPrincipais)

@app.route('/teste', methods=['POST',])
def teste():
    tipo = request.form['tipo']
    if tipo == 'Casamento':
        print (tipo)

@app.route('/adicionar-video')
def adicionarVideo():
    return render_template('Videos/adicionarVideo.html', titulo='Adicionar Videos')

@app.route('/adicionar-album')
def adicionarAlbum():
    return render_template('Albuns/adicionarAlbum.html', titulo='Adicionar Album')