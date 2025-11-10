from flask import Flask, render_template, request

app = Flask("__main__")
app.secret_key = "verySecret"


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("username")
        msg = request.form.get("message")
        return render_template("thankyou.html", user=name, message=msg)
    return render_template("feedback.html")


@app.route("/thankyou", methods=["GET"])
def thankyou():
    return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(debug=True)
