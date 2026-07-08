# Import necessary modules from Flask to build the web application, handle HTTP requests, and render HTML pages
from flask import Flask, request, render_template

# Import data manipulation libraries (numpy and pandas)
import numpy as np
import pandas as pd

# Import the StandardScaler for feature scaling (Note: It's imported here but not directly used in this file; it might be used inside the predict_pipeline)
from sklearn.preprocessing import StandardScaler

# Import custom classes from the project's source code
# CustomData maps the HTML form inputs to a format the model understands
# PredictPipeline loads the trained model and makes predictions
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Initialize the Flask application
application = Flask(__name__)

# Assign it to a shorter variable name 'app' for convenience
app = application

## Route for the home page (landing page)
@app.route('/')
def index():
    # When a user visits the root URL ('/'), render and return the 'index.html' template
    return render_template('index.html') 

# Route to handle the prediction functionality, accepting both GET (to view the page) and POST (to submit the form) requests
@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    # If the user is just loading the page (GET request)
    if request.method == 'GET':
        # Render the 'home.html' page, which likely contains the input form
        return render_template('home.html')
    
    # If the user has submitted the form (POST request)
    else:
        # 1. Gather all the data from the HTML form submitted by the user
        # Initialize the CustomData class with values extracted using request.form.get('input_name')
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            
            # Note: There appears to be a variable swap here in your original code. 
            # reading_score is fetching the 'writing_score' form input, and vice versa. 
            # You may want to correct this to: reading_score=float(request.form.get('reading_score'))
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        
        # 2. Convert the gathered form data into a Pandas DataFrame format expected by the model
        pred_df = data.get_data_as_data_frame()
        
        # Print the dataframe to the console for debugging purposes
        print(pred_df)
        print("Before Prediction")

        # 3. Initialize the prediction pipeline (which likely loads the pre-trained ML model and preprocessor)
        predict_pipeline = PredictPipeline()
        print("Mid Prediction")
        
        # 4. Pass the formatted dataframe into the prediction pipeline to get the result
        results = predict_pipeline.predict(pred_df)
        print("after Prediction")
        
        # 5. Return the 'home.html' template, passing the prediction result (first element of the results array) to be displayed on the page
        return render_template('home.html', results=results[0])
    
# Entry point for the application
if __name__=="__main__":
    # Run the Flask app on the local development server
    # host="0.0.0.0" maps it to all available IP addresses on the host machine, making it accessible externally if deployed
    app.run(host="0.0.0.0")