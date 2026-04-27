import pickle

model = pickle.load(open("alarm_model.pkl", "rb"))


def predict_status(data):

    prediction = model.predict([[
        data["temperature"],
        data["gas"],
        data["smoke"],
        data["flame"]
    ]])

    return prediction[0]