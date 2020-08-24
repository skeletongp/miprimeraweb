from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/acerca")
def acerca():
    return render_template("acerca.html")

@app.route("/perfil")
def perfil():
    return render_template("perfil.html")

if __name__=="__main__":
    app.run(debug=True)