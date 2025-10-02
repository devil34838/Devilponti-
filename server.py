from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    # Abhi simple echo reply
    ai_response = f"AI: {user_input}"
    return jsonify({"reply": ai_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
