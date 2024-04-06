import requests
from flask import Flask, render_template
import json

app = Flask(__name__)

def get_filtered_data():
    # Define the API endpoint URL
    url = "https://data.sfgov.org/resource/wg3w-h783.json"

    # Make a GET request to the API endpoint
    response = requests.get(url)
    filtered_data = []

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        unwanted_categories = ["Suicide", "Non-Criminal","Found Vehicle"]

        for entry in data:
            if (entry.get("incident_category") not in unwanted_categories and
                    entry.get("incident_description") != "Found Person" and
                    "longitude" in entry and "latitude" in entry):
                # Create a new dictionary with only the desired keys and values
                filtered_entry = {
                    "incident_category": entry["incident_category"],
                    "incident_description": entry["incident_description"],
                    "longitude": entry["longitude"],
                    "latitude": entry["latitude"]
                }
                filtered_data.append(filtered_entry)

    return filtered_data

colors = {
            'Rape': '#8B0000',
            'Arson': '#FF0000',
            'Robbery': '#DC143C',
            'Burglary': '#B22222',
            'Malicious Theft': '#FF4500',
            'Assault': '#FFA500',
            'Suspicious Occurrence': '#FF8C00',
            'Larceny Theft': '#FFD700',
            'Fraud': '#FFFF00',
            'Vandalism': '#32CD32',
            'Missing Person': '#90EE90',
            'Disorderly Conduct': '#98FB98',
            'Fire Report': '#87CEEB',
            'Other Offenses': '#B0E0E6',
            'Warrant': '#778899',
            'Other Miscellaneous': '#DCDCDC',
            'Lost Property': '#E6E6FA'
        }


@app.route('/')
def index():
    filtered_data = get_filtered_data()
    return render_template('index.html', filtered_data=json.dumps(filtered_data))

@app.route('/directions')
def directions():
    return render_template('FrontEnd.html')

if __name__ == '__main__':
    app.run(debug=True)
