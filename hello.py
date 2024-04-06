import requests
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)
filtered_data = []
# Define the API endpoint URL
url = "https://data.sfgov.org/resource/wg3w-h783.json"

# Make a GET request to the API endpoint
response = requests.get(url)
new_dict = {}
print("Start !")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    unwanted_categories = ["Suicide", "Non-Criminal",]
    

    for i in data:
        if i["incident_category"] not in unwanted_categories and "longitude" in i and i["incident_description"] != "Found Person":
        # Create a new dictionary with only the desired keys and values
            new_dict = {
                "incident_category": i["incident_category"],
                "incident_description":i["incident_description"],
                'longitude': i['longitude'],  
                'latitude': i['latitude'] 
            }
            filtered_data.append(new_dict)
            
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

else:
    print("Error:", response.status_code)

for i in filtered_data:
    print(i)

print("End !")
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/directions')
def directions():
    return render_template('FrontEnd.html')

