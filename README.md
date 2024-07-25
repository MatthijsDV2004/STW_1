SafeRoute - Finding the Safest Path
Overview
SafeRoute is a web application designed to provide users with the quickest and safest routes, especially useful for pedestrians. By leveraging the Google Maps API for routing and the San Francisco Police Department (SFPD) crime statistics API, SafeRoute ensures users can navigate the city efficiently while avoiding high-crime areas.

Features
Route Planning: Offers both car and pedestrian routing options.
Safety Integration: Combines Google Maps routing with SFPD crime data to suggest the safest paths.
User-Friendly Interface: Simple, intuitive interface for selecting start and end points, and viewing routes.
Technologies Used
Python: Backend logic and API integration.
Flask: Web framework for building the application.
HTML/CSS/JavaScript: Frontend development.
Google Maps API: Provides routing and map visualization.
SFPD Crime Data API: Supplies crime statistics for route safety analysis.
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/SafeRoute.git
cd SafeRoute
Create a Virtual Environment

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Set Up Environment Variables
Create a .env file in the project root directory and add your Google Maps API key and any other necessary configuration.

makefile
Copy code
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
SFPD_API_URL=your_sfpd_api_url
Run the Application

bash
Copy code
flask run
Access the Application
Open your web browser and go to http://127.0.0.1:5000.

Usage
Home Page:

Enter your start and end locations.
Choose your mode of transport (car or on foot).
View Routes:

The application will display the quickest route with an overlay indicating safer paths based on SFPD crime data.
Hover over the route to see detailed information about crime statistics in different areas.
Safest Path:

For pedestrian routes, the application prioritizes safety by suggesting paths through lower crime areas, even if they take slightly longer.
Contributing
We welcome contributions to SafeRoute! To contribute, please follow these steps:

Fork the repository.
Create a new branch: git checkout -b feature/your-feature-name.
Make your changes and commit them: git commit -m 'Add some feature'.
Push to the branch: git push origin feature/your-feature-name.
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Google Maps API for providing robust routing and mapping services.
San Francisco Police Department for making crime data available to the public.
Flask framework for enabling quick development of web applications.
