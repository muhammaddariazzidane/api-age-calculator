from flask import Flask, request
from flask_cors import CORS
import datetime
import locale

locale.setlocale(locale.LC_TIME, "id_ID")

app = Flask(__name__)
CORS(app)


@app.post("/calculate-age")
def calculate_age():
    data = request.get_json()

    date_of_birth = datetime.date(
        int(data["year"]), int(data["month"]), int(data["date"])
    )

    if int(data["month"]) > 12:
        return {"error": True, "message": "Month should not exceed 12"}, 400
    elif int(data["date"]) > 31:
        return {"error": True, "message": "Date should not exceed 31"}, 400
    elif date_of_birth > datetime.date.today():
        return {
            "error": True,
            "message": "The date of birth must not be later than today",
        }, 400

    age_years = datetime.date.today() - date_of_birth
    your_age_now = age_years.days // 365
    return {
        "error": False,
        "age": your_age_now,
        "date_of_birth": date_of_birth.strftime("%d %B %Y"),
        "day_of_birth": f"{date_of_birth:%A}",
    }
