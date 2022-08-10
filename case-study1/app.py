from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
import datetime

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
  "measurementId": "G-SQ8GRL04S2",
  "databaseURL": "https://case-study-664d7-default-rtdb.europe-west1.firebasedatabase.app/"}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

# -------------------ROUTS--------------------------

# home page
@app.route('/', methods = ['Get', 'POST'])
def home():
    return render_template("index.html")

# News page 
@app.route('/News', methods = ['Get', 'POST'])
def News():
    return render_template("News.html")

# contact page
@app.route('/contact', methods = ['Get', 'POST'])
def contact():
    error = ""
    if request.method == 'POST':
        print("test")
        email = request.form['email']
        full_name = request.form['full_name']
        message = request.form['message']
        rating = request.form['rating']
        time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M")

        msg = {"name": full_name, "email": email, "message": message, 'user_rate' : rating, "time" : time}
        print(msg)
        try:
            db.child("Comments").push(msg)
            return redirect(url_for('contact'))
        except:
            error = "Adding message fail"
    if db.child("Comments").get().val() != None:
        return render_template("contact.html", comments = db.child("Comments").get().val())
    
    return render_template("contact.html")
#admin comment
@app.route('/admincomment', methods = ['Get', 'POST'])
def admincomment():
    return render_template("admincomment.html")
# admin page
@app.route('/adminlogin/<string:comment>', methods = ['Get', 'POST'])
def ukkoadmin(comment):
    error = ""
    if request.method == 'POST':
        try:
            db.child("Comments").child(comment).remove()
            redirect(url_for('adminlogin', comments = db.child("Comments").get().val()))
        except:
            error = "deleting failed"
    if db.child("Comments").get().val() != None:
        return render_template("admincomment.html", comments = db.child("Comments").get().val())
    return render_template("admin.html")


# contact page
@app.route('/comments', methods = ['Get', 'POST'])
def comments():
    return render_template("contact.html")

# FAQ page
@app.route('/faq', methods = ['Get', 'POST'])
def faq():
    return render_template("faq.html")

# Blog home page
@app.route('/blog_home', methods = ['Get', 'POST'])
def blog_home():
    return render_template("blog-home.html")

# Blog post page
@app.route('/blog_post', methods = ['Get', 'POST'])
def blog_post():
    return render_template("blog-post.html")


#### dont code here
if __name__ == '__main__':
    app.run(debug=True)