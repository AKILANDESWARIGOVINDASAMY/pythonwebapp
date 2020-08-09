from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "return page!!"
@app.route("/html")
def html():
    return render_template("demo.html")



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='127.0.0.1',port=port)