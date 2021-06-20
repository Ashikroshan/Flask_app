from flask import Flask #Heroku Is LInux  Env,so we install GUNICORN

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    return "This is Flask Application"
if __name__ == "__main__":
    app.run()