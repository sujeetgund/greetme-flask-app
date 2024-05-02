from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        name = request.form.get("name")
        return render_template("index.html", name=name)

if __name__=="__main__":
    app.run(host="0.0.0.0")