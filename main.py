from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    intent = req.get("queryResult", {}).get("intent", {}).get("displayName")
    params = req.get("queryResult", {}).get("parameters", {})

    firstName = params.get("firstName", "User")
    lastName = params.get("lastName", "")
    email = params.get("email", "unknown")

    if intent == "End Chat":
        reply = f"Thanks again, {firstName} {lastName}! " \
                f"Your email is: {email}. " \
                f"This chatbot was created by Khushbu Borwal (borwalkh@mail.uc.edu). " \
                f"Have a great day!"
    else:
        reply = "Hi there! How can I help you?"

    return jsonify({"fulfillmentText": reply})
