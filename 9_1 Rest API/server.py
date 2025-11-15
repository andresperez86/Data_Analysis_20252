from flask import Flask, request, redirect, url_for, flash, jsonify
import pickle
import json
import numpy as np

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print ("LOG: predicting on input", data)
    prediction = np.array2string(model.predict(data))
    print ("LOG: returning predictions", prediction)
    return jsonify(prediction)


if __name__ == '__main__':
    modelfile = 'dtmodel.pckl'
    model = pickle.load(open(modelfile, 'rb'))
    print ("LOG: serving model", model.__class__.__name__)
    app.run(debug=True, host='0.0.0.0', port=7766)
