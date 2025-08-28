from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "ton_secret_key_ici"  # À remplacer par une vraie clé secrète

# Page d'accueil simple
@app.route("/")
def home():
    return "<h1>Bienvenue sur MediJustus !</h1>"

# Exemple de route de formulaire
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        nom = request.form.get("nom")
        flash(f"Formulaire reçu pour {nom} !")
        return redirect(url_for("home"))
    return '''
        <form method="POST">
            Nom: <input type="text" name="nom">
            <input type="submit" value="Envoyer">
        </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
