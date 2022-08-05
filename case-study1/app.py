from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'
#code here
config= {
  "apiKey": "AIzaSyBtczwHSU6cZFPprkbV2KH-nolLCwx0q5g",
  "authDomain": "case-study-664d7.firebaseapp.com",
  "projectId": "case-study-664d7",
  "storageBucket": "case-study-664d7.appspot.com",
  "messagingSenderId": "360541122608",
  "appId": "1:360541122608:web:fad092cf9abdf23e0ffdf5",
  "measurementId": "G-SQ8GRL04S2"
  "databaseURL": "https://case-study-664d7-default-rtdb.europe-west1.firebasedatabase.app/"}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()



#### dont code here
if __name__ == '__main__':
    app.run(debug=True)