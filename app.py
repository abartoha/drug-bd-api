from difflib import get_close_matches
import json
from flask import jsonify, Flask, render_template

app = Flask(__name__, template_folder='template')
app.config["DEBUG"] = True

# loads the data
data = json.load(open('brandfile.json'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/v1/all', methods=['GET'])
def api_all():
    return jsonify(data)

@app.route('/api/v1/byName/<name>', methods=['GET'])
def api_name(name):
    results = []
    for i in list(set(get_close_matches(name, [i['name'] for i in data], cutoff=0.3))):
        for j in data:
            if j['name'] == i:
                results.append(j)
    return jsonify(results)

@app.route('/api/v1/byDrug/<drug>', methods=['GET'])
def api_drug(drug):
    results = []
    for i in list(set(get_close_matches(drug, [i['drug'] for i in data], cutoff=0.3))):
        for j in data:
            if j['drug'] == i:
                results.append(j)
    return jsonify(results)

if __name__=="__main__":
    app.run()