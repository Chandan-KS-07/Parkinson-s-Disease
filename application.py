from flask import Flask, request, render_template
import pickle
import numpy as np

application = Flask(__name__)
app = application

model = pickle.load(open("Parkinson_disease.pkl", "rb"))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    result = ""
    if request.method == 'POST':
        MDVP_Fo_Hz = float(request.form.get("MDVP_Fo_Hz"))
        MDVP_Fhi_Hz = float(request.form.get("MDVP_Fhi_Hz"))
        MDVP_Flo_Hz = float(request.form.get("MDVP_Flo_Hz"))
        MDVP_Jitter_percent = float(request.form.get("MDVP_Jitter_percent"))
        MDVP_Jitter_Abs = float(request.form.get("MDVP_Jitter_Abs"))
        MDVP_RAP = float(request.form.get("MDVP_RAP"))
        MDVP_PPQ = float(request.form.get("MDVP_PPQ"))
        Jitter_DDP = float(request.form.get("Jitter_DDP"))
        MDVP_Shimmer = float(request.form.get("MDVP_Shimmer"))
        MDVP_Shimmer_dB = float(request.form.get("MDVP_Shimmer_dB"))
        Shimmer_APQ3 = float(request.form.get("Shimmer_APQ3"))
        Shimmer_APQ5 = float(request.form.get("Shimmer_APQ5"))
        MDVP_APQ = float(request.form.get("MDVP_APQ"))
        Shimmer_DDA = float(request.form.get("Shimmer_DDA"))
        NHR = float(request.form.get("NHR"))
        HNR = float(request.form.get("HNR"))
        RPDE = float(request.form.get("RPDE"))
        DFA = float(request.form.get("DFA"))
        spread1 = float(request.form.get("spread1"))
        spread2 = float(request.form.get("spread2"))
        D2 = float(request.form.get("D2"))
        PPE = float(request.form.get("PPE"))

        predict_data = [[MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent, MDVP_Jitter_Abs,
                         MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3,
                         Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2,
                         D2, PPE]]

        predict = model.predict(predict_data)

        if predict[0] == 1:
            result = 'Person Has Parkinson Disease'
        else:
            result = 'Person Has No Parkinson Disease'

        return render_template('home.html', result=result)

    else:
        return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/features')
def features():
    return render_template('features.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
