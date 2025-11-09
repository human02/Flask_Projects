from flask import Flask, request, redirect, url_for, Response, session, render_template

app = Flask(__name__)
app.secret_key = "verysecret"

valid_users = {"admin": "12345", "john": "doe", "hello": "world"}


# Homepage
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # basic check
        if username in valid_users and password == valid_users[username]:
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            # default is JSON, hence mime used to send text/plain response
            return Response(
                "Invalid Credentials, Please try again!", mimetype="text/plain"
            )


@app.route("/welcome", methods=["GET"])
def welcome():
    if "user" in session:
        return render_template("welcome.html")
    else:
        return "Page not Found 404"


@app.route("/logout")
def logout():
    session.pop("user")
    return render_template("logout.html")


if __name__ == "__main__":
    app.run(debug=True)
