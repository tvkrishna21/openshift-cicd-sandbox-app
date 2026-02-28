from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"Tekton based CI/CD Sandbox App - Version: {os.getenv('VERSION', 'dev')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
