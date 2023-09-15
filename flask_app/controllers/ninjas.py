#only deals with routes as controllers
from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo_model import dojo
from flask_app.models.ninja_model import ninja

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html", ninjas=ninjas.get_all())

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    #ninjas = ninjas()
    #print(ninjas)
    return render_template("dojos.html")



@app.route('/show')
def show():
    return render_template("ninjas.html", dojo=dojo)

@app.route('/new')
def new_ninja():
    return render_template("new_ninja.html", ninja=ninja)


@app.route('/register',methods=['POST'])
def register():
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
    }
    id = ninja.save(data)
    return redirect('/Homescreen')

#@app.route('/ninja/new', methods = ["GET"])
#def new():
    #user = User.get_all()
    #print(user)
#    return render_template("new_ninja.html")

#@app.route('/create_ninja', methods=["POST"])
#def create_ninja():
#    ninjas.save(request.form)
    # Don't forget to redirect after saving to the database.
#    return redirect('/ninjas')


#@app.route('/ninjas')
#def ninjas():
#    return render_template("ninjas.html", ninjas=ninjas.get_all())
if __name__ == "__main__":
    app.run(debug=True)