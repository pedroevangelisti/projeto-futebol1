from flask import Flask, render_template, request, jsonify 
import requests 

app = Flask(__name__)

@app.route ('/') #/ leva pro home 
def home():
    return render_template('index.html')

@app.route ('/search', methods = ['POST']) #dados enviados por forms ou algo do tipo 
def search():
    team_name= request.form ['team']
    return jsonify({"time": team_name})
    
from flask import Flask, request, jsonify

# Vercel expects a function called `handler`
def handler(request):
    if request.method == "POST":
        team_name = request.form.get("team", "")
        return jsonify({"time": team_name})
    else:
        return jsonify({"error": "Only POST method allowed."}), 405

