from flask flask,render_tempalate

app = Flask(__name__)
@app.route("/")
def top():
    return render_tempalate("index.html")

if __name__ == "__main__":
    app.run(debug=True)