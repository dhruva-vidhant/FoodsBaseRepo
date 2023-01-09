from flask import render_template
from flask import Flask
import db
from flask import request
from keywordfind import *
from calories import *
from demo import * 
import search
#import requests
app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sellers.html')
def sellers():
    return render_template('sellers.html')
@app.route('/exercise.html')
def exercise():
    return render_template('exercise_data.html')
@app.route('/symptoms.html')
def symptoms():
    return render_template('symptoms.html')
@app.route("/script.js")
def jsimport():
    return render_template("script.js")
@app.route('/demoprocess', methods=["GET","POST"])
def demoprocess():
    list = []
    print("RUNNING")
    symp = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue',
                                  'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss',
                                  'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration',
                                  'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever',
                                  'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
                                  'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
                                  'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
                                  'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness',
                                  'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
                                  'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes',
                                  'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma',
                                  'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples',
                                  'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']
    print("running")
    for x in symp:
        print(x)
        try:
            if request.form[x] == "on":
                list.append(x)
        except Exception:
            print("pass")
            pass
    print("verification complete.")
    print(list)
    print("Processing Symptoms")
    data = predict_disease_from_symptom(list)
    return render_template("symptoms_results.html", list=list, data=data)

@app.route('/exerciseprocess', methods=["GET","POST"])
def processexcercise():
    QUERY = request.form["exer_description"]
    print(QUERY)
    GENDER = request.form["gender"]
    print(GENDER)
    AGE = request.form["age"]
    print(AGE)
    WEIGHT = request.form["weight"]
    print(WEIGHT)
    HEIGHT = request.form["height"]
    print(HEIGHT)
    data = calories(QUERY, GENDER, AGE, WEIGHT, HEIGHT)
    print(data)
    return render_template('exercise_results.html', data=data)

@app.route("/buydata", methods=["GET","POST"])
def bdata():
    data = request.form["location"]
    print(data)
    return render_template("buyers.html", data=data)
@app.route("/admin")
def admin():
    print("Admin Panel verification.")
    print("Retaining request until verified.")
    u = input("Do you allow this request? (y)es or (n)o ->")
    if u == "y":
        print("Request accepted, rendering.")
        return render_template("adminaccess.html")
    else:
        print("Request denied.")
        reason = input("Reason ->")
        if reason == "":
            return("6909 - uwuDenied")
        else:
            return(reason)
@app.route('/access', methods=['GET', 'POST'])
def access():
    print("-")

@app.route("/buyers.html", methods=["GET", "POST"])
def buyers():
    print("Buyers Access")
    return render_template("buyers.html")

@app.route("/index.php", methods=["GET", "POST"])
def indexphp():
    print("index.php")
    return render_template("index.php")
@app.route("/token_generator.php")
def tkngen():
    return render_template("token_generator.php")
@app.route("/script.js")
def scriptjs():
    return render_template("script.js")
@app.route('/submit', methods=['POST'])
def submit():
    print("access")
    ret = request.form['ret']
    print(ret)
    keys = get_keywords(ret)
    print(keys)
    return render_template('submit.html', keys=keys)

@app.route('/title/<title>')
def searchByTitle(title):
    return search.searchByTitle(title)

@app.route('/keyword/<keyword>')
def searchByKeyword(keyword):
    x = search.searchByKeyword(keyword)
    print(x, keyword)
    return x

@app.route('/food_page/<id>')
def food_page(id):
    reader = open('templates/food2.html', 'r')
    contents = reader.read()
    info = db.get_info(id)
    print(info[1], info[2])
    contents = contents.replace('REPLACE WITH FOOD NAME', info[1])
    contents = contents.replace('REPLACE WITH KEYWORDS', str(info[8]))
    contents = contents.replace('REPLACE WITH PRICE', str(info[3]))
    contents = contents.replace('REPLACE WITH DESC', str(info[2]))
    return contents





    
