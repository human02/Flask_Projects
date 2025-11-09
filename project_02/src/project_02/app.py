from flask import Flask, request, render_template, Response, session

app = Flask(__name__)
app.secret_key = "verysecret"

marksheet = [
    {
        "username": "a.johnson",
        "name": "Alice Johnson",
        "marks": {"maths": 95, "history": 88, "science": 92},
        "is_topper": True,
    },
    {
        "username": "b.smith",
        "name": "Bob Smith",
        "marks": {"maths": 78, "history": 82, "science": 75},
        "is_topper": False,
    },
    {
        "username": "c.brown",
        "name": "Charlie Brown",
        "marks": {"maths": 85, "history": 90, "science": 88},
        "is_topper": False,
    },
]


users = {"a.johnson": "pass", "b.smith": "pass", "c.brown": "pass"}


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        user = request.form.get("username")
        passwrd = request.form.get("password")
        session["user"] = user
        if user in users and users[user] == passwrd:
            for it in marksheet:
                if it["username"] == user:
                    name = it["name"]
                    isTopper = it["is_topper"]
                    student_marks = [
                        (key.capitalize(), val) for key, val in it["marks"].items()
                    ]
                    student_marks.sort(key=lambda x: -x[1])
            return render_template(
                "welcome.html",
                marksheet=student_marks,
                name=name,
                isTopper=isTopper,
            )
        else:
            return Response("Invalid Credentials", mimetype="text/plain")


@app.route("/logout")
def logout():
    session.pop("user")
    return render_template("logout.html")


if __name__ == "__main__":
    app.run(debug=True)
