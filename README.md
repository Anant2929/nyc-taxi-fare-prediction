🚖 NYC Taxi Fare Prediction

Welcome to the NYC Taxi Fare Prediction project! This is a cutting-edge machine learning application designed to predict taxi fares in New York City with precision and ease. Whether you're a tourist planning a ride or a data enthusiast exploring predictive modeling, this app has something for you! 🚕

✨ Project Highlights

Accurate Fare Predictions: Estimate taxi fares based on pickup/dropoff locations, passenger count, and trip timing.
Powerful ML Models: Leverages Ridge Regression and XGBoost for robust predictions.
Interactive UI: Built with Streamlit, featuring a sleek dark-themed interface with glassmorphism design.
Map Visualization: Visualize your trip on an interactive map with pickup and dropoff markers, powered by Folium.
Real-World Application: Deployed on Streamlit Cloud for global access.


🛠️ Features

Predict Fares Dynamically: Input your trip details (pickup/dropoff locations, passenger count, and pickup time) to get an instant fare estimate.
NYC Landmarks Support: Choose from popular NYC locations like Times Square, Central Park, and the Empire State Building.
Trip Visualization: See your route on a map with a blue polyline connecting pickup and dropoff points.
Fare Breakdown: Get a detailed breakdown of the fare, including base fare, distance, and time components.
Responsive Design: A modern, user-friendly interface with a dark theme and 3D touch effects.


📸 Screenshots



Home Page
![image](https://github.com/user-attachments/assets/336395d8-e1f8-4827-89c3-735b33ce4238)

Fare Prediction
![image](https://github.com/user-attachments/assets/23396678-df68-42bb-ab2b-80af5ddfdb49)


🧠 Machine Learning Details
Models Used

Ridge Regression: A linear model with L2 regularization to handle multicollinearity.
XGBoost: A gradient-boosting model with tuned hyperparameters for superior performance.

Features Engineered

Trip Distance: Calculated using the Haversine formula between pickup and dropoff coordinates.
Time Features: Extracted from pickup datetime (year, month, day, weekday, hour).
Landmark Distances: Distances to key NYC landmarks (e.g., JFK, LaGuardia) for better fare estimation.

Performance

Achieved a validation RMSE of ~3.90 with XGBoost, ensuring accurate predictions.


⚙️ Tech Stack

Python: Core language for data processing and modeling.
Pandas & NumPy: Data manipulation and numerical computations.
Scikit-learn: For Ridge Regression and preprocessing.
XGBoost: For gradient-boosting model.
Streamlit: Interactive web app framework.
Folium & Streamlit-Folium: Map visualization.
GitHub & Streamlit Cloud: Version control and deployment.


🚀 Setup & Installation
Get started with the project in just a few steps!

Clone the Repository:
git clone https://github.com/anant2929/nyc-taxi-fare-prediction.git
cd nyc-taxi-fare-prediction


Create a Virtual Environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Run the App Locally:
streamlit run app.py

Open your browser and go to http://localhost:8501 to see the app in action!



🌐 Live Demo
Experience the app live on Streamlit Cloud!👉 NYC Taxi Fare Predictor (https://anant2929-nyc-taxi-fare-prediction-app-1dkfx0.streamlit.app/)

📜 Usage

Select Locations: Choose your pickup and dropoff locations from a list of popular NYC landmarks.
Enter Trip Details: Input the number of passengers and pickup time.
Visualize Your Trip: See your route on an interactive map.
Predict Fare: Click the “Predict Fare” button to get an estimated fare with a detailed breakdown.


🤝 Contributing
Contributions are welcome! If you’d like to improve this project, please:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.


📧 Contact
Have questions or feedback? Reach out to me!  

GitHub: anant2929  
Email: anantgupta526@gmail.com  
LinkedIn: (https://www.linkedin.com/in/anant-gupta-87211a19b/)


🌟 Acknowledgments

Inspired by real-world taxi fare prediction challenges.
Thanks to the Streamlit community for an amazing framework.
Built with ❤️ by Anant.


Live Demo: NYC Taxi Fare Predictor(https://anant2929-nyc-taxi-fare-prediction-app-1dkfx0.streamlit.app/)
