from flask import Flask, render_template, jsonify, request
import requests 

app = Flask(__name__)

@app.route ('/') #/ leva pro home 
def home():
    return render_template('index.html')

@app.route ('/search', methods = ['POST']) #dados enviados por forms ou algo do tipo 
def search():
    team_name= request.form.get ('team')
    return jsonify({"time": team_name})
    


