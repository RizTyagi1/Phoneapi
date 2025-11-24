from flask import Flask, request
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

app = Flask(__name__)

@app.route("/info")
def get_info():
    number = request.args.get("number", "").replace(" ", "")

    if not number.startswith("+"):
        number = "+91" + number

    try:
        phone = phonenumbers.parse(number)
        return {
            "number": number,
            "location": geocoder.description_for_number(phone, "en"),
            "carrier": carrier.name_for_number(phone, "en"),
            "timezone": list(timezone.time_zones_for_number(phone))
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
