from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo_model import Dojo


@app.route('/dojo', methods=['POST'])
def submit():
    #get_all suppose to be here somewhere
    name = request.form['name']
    return render_template("index.html", name=name)

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    Dojo.save(request.form)
    #Don't forget to redirect after saving to the database.
    return redirect('/')

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    data = {
        "name": request.form['name'],
    }
    Dojo.save(data)
    return redirect('/')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    Dojo=Dojo.get_dojo_with_ninja(id)
    print(Dojo)
    return render_template("index.html", dojos=Dojo)

#how to get this app route above to display next to the form in index html 






    #dojo.save(request.form)
    #data = data
    #dojo.id =  dojo.save(data)
    #return redirect("index.html",dojo=dojo)

#@app.route('/friends/create', methods=['POST'])
#def create():
#    Friend.save(request.form)
#    return redirect('/')