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

@app.route('/')
def index():
    filtered_data = get_filtered_data()
    return render_template('index.html', filtered_data=json.dumps(filtered_data))

@app.route('/directions')
def directions():
    return render_template('FrontEnd.html')

if __name__ == '__main__':
    app.run(debug=True)
