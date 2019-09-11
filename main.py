from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy
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
   
    
    def __init__(self, name, credScore):
       self.name = name
       self.credScore = credScore


       name = 'Nicole Duncan'
       credScore = 600
       new_app_object = Applications(name, credScore)
       db.session.add(new_app_object)      
       db.session.commit()

       name = 'Beth Burke'
       credScore = 700
       new_app_object = Applications(name, credScore)
       db.session.add(new_app_object)      
       db.session.commit()

       name = 'Derek Scott'
       credScore = 800
       new_app_object = Applications(name, credScore)
       db.session.add(new_app_object)      
       db.session.commit()

       print("line 45")

@app.route('/test', methods=['POST', 'GET'])
def test():

      if request.method == 'POST':
       
        score = request.form['score']
     
      return render_template('altervar.html',score="score")  


    

@app.route('/results', methods=['POST', 'GET'])
def results():

      if request.method == 'POST':
      
            applicants = db.session.query(Applications).all()
    
            counter = 1
            loop_queries = []
            for objects in applicants:
                  loop_query = Blog.query.filter_by(credScore).first()
                  if loop_query > score: 
                        print("eligible")
                  

      return render_template('results.html', name=name, credScore=credScore)  

"""     

@app.route('/display/<int:post_id>', methods=['POST', 'GET'])
def display(post_id):

      display_list = []

      displayed_blog_object = Blog.query.filter_by(id=post_id).first()
      display_list.append(displayed_blog_object)
     
      return render_template('blogdisplay.html', display_list=display_list)


@app.route('/', methods=['POST', 'GET'])
def index():

    blogs = db.session.query(Blog).all()
    
    counter = 1
    loop_queries = []
    for objects in blogs:
      loop_query = Blog.query.filter_by(id=counter).first()
      counter += 1
      loop_queries.append(loop_query)
    
    
    return render_template('blog.html',loop_queries=loop_queries)
  
"""


if __name__ == '__main__':
    app.run()
