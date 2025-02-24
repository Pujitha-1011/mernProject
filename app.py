import pickle
import numpy as np # type: ignore
from flask import Flask, render_template, request
app = Flask(__name__)

# Load the trained model
with open("random_forest_pkl.pkl", "rb") as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data from user input
        features = [
            float(request.form['N']),
            float(request.form['P']),
            float(request.form['K']),
            float(request.form['ph']),
            float(request.form['ec']),
            float(request.form['oc']),
            float(request.form['S']),
            float(request.form['zn']),
            float(request.form['fe']),
            float(request.form['cu']),
            float(request.form['Mn']),
            float(request.form['B'])
        ]

        # Convert input data to numpy array and reshape for prediction
        input_data = np.array([features]).reshape(1, -1)

        # Make prediction using the loaded model
        prediction = model.predict(input_data)[0]  # Get the predicted class

        # Convert numerical prediction to readable text (Assuming 1 = Fertile, 0 = Infertile)
        result_text = "Fertile" if prediction == 1 else "Infertile"

        return render_template('result.html', prediction=result_text)
    
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
