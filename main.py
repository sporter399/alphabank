from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean

import os
import sqlite3

app = Flask(__name__)

app.config['DEBUG'] = True
project_dir = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(project_dir, "alphabank.db"))
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Applications(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    credScore = db.Column(db.Integer())
    monthlyIncome = db.Column(db.Integer())
    eligible = db.Column(db.Boolean)
    
   
    
    def __init__(self, name, credScore, monthlyIncome):
       self.name = name
       self.credScore = credScore
       self.monthlyIncome = monthlyIncome
       self.eligible = False
       

def createDataBase():
       name = 'Nicole Duncan'
       credScore = 600
       monthlyIncome = 4000
       new_app_object = Applications(name, credScore, monthlyIncome)
       print("newappobjectline30     " + str(new_app_object))
       db.session.add(new_app_object)      
       db.session.commit()

       name = 'Beth Burke'
       credScore = 700
       monthlyIncome = 2000
       new_app_object = Applications(name, credScore, monthlyIncome)
       db.session.add(new_app_object)      
       db.session.commit()

       name = 'Derek Scott'
       credScore = 800
       monthlyIncome = 7000
       new_app_object = Applications(name, credScore, monthlyIncome)
       db.session.add(new_app_object)      
       db.session.commit()

       print("line 45")

       return



@app.route('/test', methods=['POST', 'GET'])
def test():

            return render_template('altervar.html',score="Credit Score:", monthly_income="Monthly Income:")  


@app.route('/results', methods=['POST', 'GET'])
def results():

      if request.method == 'POST':
            
      
            applicants = db.session.query(Applications).all()         
            score = request.form['score']
            monthly_income = request.form['monthly_income']
           
            
            for object in applicants:
                  
                  if (object.credScore > int(score)) and (object.monthlyIncome > int(monthly_income)):
                        print("eligible")

                  else:
                        print("ineligible")
                  

                 
      return render_template('results.html', score="score", monthly_income="monthly_income") 


@app.route('/', methods=['POST', 'GET'])
def index():

   
    createDataBase()
    
    return render_template('altervar.html')


if __name__ == '__main__':
    db.create_all()
    app.run()
