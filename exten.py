from flask import Flask

app = Flask(__name__)


# Template 
# Criar o site 

@app.route("/")
def homepage():
    return "Primeiro site"
    

@app.route("/Contatos")
def contatos():
    return "<p>Número: (21)99999-9999</p><p>E-mail: iasjisis@gmail.com</p>"



    
# Colocar o site no ar
app.run(debug=True)

