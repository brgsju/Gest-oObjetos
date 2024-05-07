

from flask import Flask, render_template

app = Flask(__name__)

# criar a primeira página do site
# route -> endereçamento. Nesse caso: GestaodeObjetos.com/
# função -> o que vai ser exibido na página 

@app.route("/") # -> vai direto para homepage. Pode ser também "/home"
def homepage():
    return render_template("homepage.html") 

@app.route("/login")
def login():
    return render_template("login.html") 

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario = nome_usuario) 
 

# colocar o site no ar 
if __name__ == "__main__":
    app.run(debug=True)