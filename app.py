from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple rule-based dental clinic chatbot (no external API)
def dental_bot_reply(user_text: str) -> str:
    text = user_text.lower()

    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Hello! Welcome to our dental clinic. How can I help you today?"

    if "timing" in text or "time" in text or "open" in text or "closing" in text:
        return "Our clinic is open Monday to Saturday, 10:00 AM to 8:00 PM."

    if "appointment" in text or "book" in text or "slot" in text:
        return "You can book an appointment by calling us or sharing your preferred date and time here."

    if "location" in text or "address" in text or "where" in text:
        return "We are located near the main market area in your city. Landmarks can be added here."

    if "fees" in text or "charge" in text or "cost" in text or "price" in text:
        return "Our consultation fee starts from Rs. 300. Treatment charges depend on the procedure."

    if "braces" in text or "aligner" in text:
        return "We provide metal, ceramic, and clear aligner braces. The dentist will suggest the best option after a checkup."

    if "cleaning" in text or "scaling" in text:
        return "Teeth cleaning/scaling usually takes 20–30 minutes and is recommended once or twice a year."

    if "root canal" in text or "rct" in text:
        return "Root canal treatment is done under local anaesthesia and usually requires 1–3 sittings depending on the tooth."

    if "emergency" in text or "pain" in text or "toothache" in text:
        return "If you have severe pain or swelling, please visit the clinic as soon as possible or call the emergency number."

    if "services" in text or "treatment" in text:
        return "We offer checkups, fillings, root canals, crowns, braces, teeth whitening, and child dental care."

    return "I am a simple dental clinic assistant. Please ask about timings, location, appointments, fees, or treatments."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    reply = dental_bot_reply(user_msg)
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)