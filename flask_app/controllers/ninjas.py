#only deals with routes as controllers
from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.ninja_model import Ninja

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninjas():
    return render_template("ninjas.html", ninjas=ninjas)


@app.route('/ninja/create', methods=['POST'])
def create():
    data = {
        "first_name": request.form["first_name"]

    }
    Ninja.save(data)
    return redirect("index.html",ninja=Ninja)

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