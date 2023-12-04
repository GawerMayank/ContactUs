from flask import Flask, render_template, request,session
from flask_sqlalchemy import SQLAlchemy
import MySQLdb

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/Contactus?unix_socket=/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock'
db=SQLAlchemy(app)

class contacts(db.Model):
        sno = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(50), nullable=False)
        phone = db.Column(db.String(12), nullable=False)
        message = db.Column(db.String(500), nullable=False)

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'POST':
         email = request.form.get('email')
         phone = request.form.get('phone')
         message = request.form.get('message')
         new_contact = contacts(email=email, phone=phone, message=message)
         db.session.add(new_contact)
         db.session.commit()
         return "Submit success"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)