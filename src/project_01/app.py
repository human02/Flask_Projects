from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        print(
            f"\n{'#'*50}\nThis is the Home Page of the Website.\n\nWelcome! Hello World!\n"
        )
        return "Hello World, Flask with Poetry is up!"
    if request.method == "POST":  # curl -X POST "http://127.0.0.1:5000/?name=John"
        print(f"\nUser entered some data")
        name = request.args.get("name", type=str)
        return f"Thank you {name} for entering the details. Welcome {name}"


@app.route("/about")
def about():
    return "This is the About US page."


@app.route("/login")
def login():
    return "Login Page"


if __name__ == "__main__":
    app.run(debug=True)
