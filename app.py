import joblib
from flask import Flask, request, render_template

app = Flask(__name__)
model = joblib.load('cell_model.ml')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    prediction = model.predict([[int(request.form['battery_power']),
                            int(request.form['front_camera']),
                            int(request.form['4g']),
                            int(request.form['internal_memory']),
                            int(request.form['mobile_weight']),
                            int(request.form['no_cores_processor']),
                            int(request.form['primary_camera']),
                            int(request.form['pixel_height_resolution']),
                            int(request.form['pixel_width_resolution']),
                            int(request.form['ram']),
                            int(request.form['screen_height']),
                            int(request.form['screen_width']),
                            ]])
    output = str(round(prediction[0],2))
        
    return render_template('index.html',prediction='Cell Phone Price Range should be $ {}'.format(output))
                           

if __name__ == "__main__":
    app.run(debug=True)
