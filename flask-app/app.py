from flask import Flask , request, render_template
import pickle
from  processingu_utility import normalize_text
import mlflow, dagshub

mlflow.set_tracking_uri("https://dagshub.com/DHRUV-29-10-3/mlops-mini-project.mlflow")
dagshub.init(repo_owner='DHRUV-29-10-3', repo_name='mlops-mini-project', mlflow=True)

vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))
model_name = "my_model"
model_version = 3

model_uri = f"models:/{model_name}/{model_version}"
model = mlflow.pyfunc.load_model(model_uri=model_uri)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", result = None)

@app.route("/predict", methods = ["POST"])
def predict():
    text = request.form["text"]
    
    #cleaning the data 
    text = normalize_text(text)

    # bow 
    features = vectorizer.transform([text]) 


    # predictionn
    result = model.predict(features)

    #show results 
    return render_template("index.html", result = result[0])


app.run(debug=True, port = 8000)