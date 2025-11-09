from flask import Flask, request, redirect, url_for, Response, session

app = Flask(__name__)
app.secret_key = "verysecret"


# Homepage
@app.route("/", methods=["GET"])
def home():
    return f"""
    <h2>Welcome to the Homepage</h2>
    Click <a href={url_for("login")}>here</a> to login.
    """


# - use for Login
@app.route("/login", methods=["GET", "POST"])
def login():
    session.pop("user", None)
    if request.method == "GET":
        return f"""
                <h2> Login Page</h2>
                <form method="POST">
                <label>Username:</label>
                        <input type="text" name="username" required>
                        <br><br>
                        <label>Password:</label>
                        <input type="password" name="password" required>
                        <br><br>
                        <button type="submit">Login</button>
                </form>
                """

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
        return f"""
        <h2>Welcome {session['user']}!</h2>
        <p> Click below to logout </p>
        <a href={url_for('login')}>Logout</a>
        """
    else:
        return "Page not Found 404"


if __name__ == "__main__":
    app.run(debug=True)
