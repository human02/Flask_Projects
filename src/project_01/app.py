from flask import Flask, request, redirect, url_for, Response, session, render_template

app = Flask(__name__)
app.secret_key = "verysecret"


# Homepage
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


# - use for Login
@app.route("/login", methods=["GET", "POST"])
def login():
    session.pop("user", None)
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # basic check
        if username == "admin" and password == "12345":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response(
                "Invalid Credentials, Please try again!", mimetype="text/plain"
            )


@app.route("/welcome", methods=["GET"])
def welcome():
    if "user" in session:
        return render_template("welcome.html")
    else:
        return "Page not Found 404"


if __name__ == "__main__":
    app.run(debug=True)
