import json
from flask import Flask, request, render_template
from models.trivia import Trivia

app = Flask(__name__)
apiKey = "<API_KEY>"


@app.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        trivia = Trivia(apiKey)
        result = trivia.fetch()
        isValid = result["status"]
        if isValid:
            message = json.loads(result["msg"])[0]["fact"]
            return render_template("index.html", trivia=message)
        else:
            return "Failed to fetch trivia", 400

if __name__ == "__main__":
    app.run(debug=True)
