from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        return redirect(url_for("success", user=username))
    return render_template("login.html")

@app.route("/success")
def success():
    user = request.args.get("user", "Usuário")
    return render_template("success.html", user=user)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
