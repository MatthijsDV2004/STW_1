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
    # Print the first few records
    # for i in data:
        # for key,value in i.items():  # Print the first 5 records for demonstration
                # print(key,":" , value)
            # if(key == "incident_category"):
                # dict =  {
                #             "incident_category" : key[incident_category],
                #             'longitude': key[longitude],  
                #             'latitude': key[latitude] 
                #         }
                # filtered_data.append(dict)
            

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

