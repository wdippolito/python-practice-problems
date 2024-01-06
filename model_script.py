import json
import joblib
import numpy as np

# Load the model (Assuming the model is uploaded with the Lambda deployment package)
model = joblib.load('/path/to/logistic_regression_model.joblib')

def lambda_handler(event, context):
    # Parse input data from event
    input_data = np.array([event['features']])  # Replace 'features' with your input data key
    
    # Make a prediction
    prediction = model.predict(input_data)
    
    # Return the prediction
    return {
        'statusCode': 200,
        'body': json.dumps({'prediction': prediction.tolist()})
    }