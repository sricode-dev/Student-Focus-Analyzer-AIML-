from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start_session():
    data = request.get_json()
    apps = data.get("apps", [])

    if not apps:
        return jsonify({"error": "Please select at least one study app"}), 400

    return jsonify({"message": "Study Session Started"})

# 🔥 NEW ROUTE FOR BADGE MESSAGE
@app.route("/badge", methods=["POST"])
def badge_message():
    minutes = request.json.get("minutes", 0)

    if minutes >= 60:
        msg = "🏆 Excellent Focus"
    elif minutes >= 45:
        msg = "👍 Good Focus"
    elif minutes >= 30:
        msg = "✨ Focus Great"
    else:
        msg = ""

    return jsonify({"message": msg})

if __name__ == "__main__":
    app.run(debug=True)