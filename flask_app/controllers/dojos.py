from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo_model import dojo





@app.route('/show')
def show():
    return render_template("dojos.html", dojo=dojo)

@app.route('/dojo/create', methods=['POST'])
def create():
    #dojo.save(request.form)
    #data ={ 
    #    "name": request.form['name']
    #}
    #dojo.id =  dojo.save(data)
    return redirect("dojos.html",dojo=dojo)

#@app.route('/friends/create', methods=['POST'])
#def create():
#    Friend.save(request.form)
#    return redirect('/')