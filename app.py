# app.py - Flask Backend for VaastuGyan App
from flask import Flask, render_template, jsonify
from datetime import datetime
import json

app = Flask(__name__)

def get_mock_panchang_data():
    """Mock Panchang data - Replace with real API call here"""
    # TODO: Replace with real Panchang API like drikpanchang.com API
    today = datetime.now().strftime("%B %d, %Y")
    mock_data = {
        "date": today,
        "tithi": "Dwadashi",
        "nakshatra": "Uttara Phalguni",
        "auspicious": {
            "abhijit_muhurat": "11:48 AM - 12:36 PM"
        },
        "avoid": {
            "rahu_kaal": "7:30 AM - 9:00 AM"
        }
    }
    return mock_data

@app.route('/')
def home():
    panchang = get_mock_panchang_data()
    rashi = 'मेष'  # Default - JS handles persistence
    return render_template('index.html', panchang=panchang, rashi=rashi)

@app.route('/vastu')
def vastu():
    tips = [
        {"category": "Home", "tip": "Main entrance should face North or East"},
        {"category": "Office", "tip": "Boss desk should face North-East"},
        {"category": "Health", "tip": "Bedroom in South-West corner"},
        {"category": "Home", "tip": "Kitchen in South-East direction"},
        {"category": "Office", "tip": "Cash box in North direction"},
        {"category": "Health", "tip": "Water elements in North-East"},
        {"category": "Home", "tip": "Pooja room in North-East corner"}
    ]
    return render_template('vastu.html', tips=tips)

@app.route('/compass')
def compass():
    directions = {
        "N": "उत्तर (North) - Kubera",
        "NE": "ईशान (North-East) - Ishaan",
        "E": "पूर्व (East) - Indra", 
        "SE": "आग्नेय (South-East) - Agni",
        "S": "दक्षिण (South) - Yama",
        "SW": "नैऋत्य (South-West) - Niruti",
        "W": "पश्चिम (West) - Varun",
        "NW": "वायव्य (North-West) - Vayu"
    }
    return render_template('compass.html', directions=directions)

@app.route('/horoscope')
def horoscope():
    zodiacs = [
        {"name": "मेष (Aries)", "symbol": "♈", "prediction": "उत्तम दिन रहेगा। धन लाभ के योग।"},
        {"name": "वृषभ (Taurus)", "symbol": "♉", "prediction": "परिवार में सुख शांति।"},
        {"name": "मिथुन (Gemini)", "symbol": "♊", "prediction": "नया कार्य प्रारंभ करने का शुभ समय।"},
        {"name": "कर्क (Cancer)", "symbol": "♋", "prediction": "स्वास्थ्य का ध्यान रखें।"},
        {"name": "सिंह (Leo)", "symbol": "♌", "prediction": "नेतृत्व के अवसर मिलेंगे।"},
        {"name": "कन्या (Virgo)", "symbol": "♍", "prediction": "अध्ययन में सफलता।"},
        {"name": "तुला (Libra)", "symbol": "♎", "prediction": "विवाह योग संभव।"},
        {"name": "वृश्चिक (Scorpio)", "symbol": "♏", "prediction": "व्यापार में लाभ।"},
        {"name": "धनु (Sagittarius)", "symbol": "♐", "prediction": "यात्रा का योग।"},
        {"name": "मकर (Capricorn)", "symbol": "♑", "prediction": "करियर में प्रगति।"},
        {"name": "कुंभ (Aquarius)", "symbol": "♒", "prediction": "मित्रों का सहयोग।"},
        {"name": "मीन (Pisces)", "symbol": "♓", "prediction": "आध्यात्मिक उन्नति।"}
    ]
    return render_template('horoscope.html', zodiacs=zodiacs)

# Add this route to app.py (add before if 
@app.route('/set_rashi/<rashi>')
def set_rashi(rashi):
    # In production, save to session/cookie/database
    return jsonify({"status": "success", "rashi": rashi})

if __name__ == '__main__':
    app.run(debug=False)
