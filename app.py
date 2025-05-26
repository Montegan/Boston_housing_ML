import pickle
from flask import Flask, request, app, jsonify, url_for, render_template  # type: ignore
import numpy as np
import pandas as pd

app = Flask(__name__)
# Load Model
regmodel = pickle.load(open("regmodel.pkl", "rb"))
scaller = pickle.load(open("scaller.pkl", "rb"))


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/second")
def second():
    return render_template("second.html")


@app.route("/predict_api", methods=['POST'])
def predictions():
    data = request.json["data"]
    print(data)
    data_arr = np.array(list(data.values())).reshape(1, -1)
    data_scalled = scaller.transform(data_arr)
    reg_output = regmodel.predict(data_scalled)
    print(reg_output[0])
    return jsonify(reg_output[0])


@app.route('/predict', methods=["POST"])
def make_prediction():
    data = [float(x) for x in request.form.values()]
    np_data = np.array(data).reshape(1, -1)
    scalled_data = scaller.transform(np_data)
    predicted_price = regmodel.predict(scalled_data)
    print(np_data.shape)
    return render_template("home.html", predicted="The predicted value is {}".format(predicted_price[0]))


if __name__ == "__main__":
    app.run(debug=True)
