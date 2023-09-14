#only deals with routes as controllers
from flask import render_template, redirect, request
from flask_app import app
#from ninjas import ninja



@app.route("/")
def index():
    # call the get all classmethod to get all friends
    #ninjas = ninjas()
    #print(ninjas)
    return render_template("dojos.html")

#@app.route('/ninjas')
#def ninjas():
#    return render_template("ninjas.html", ninjas=ninjas.get_all())

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

if __name__ == "__main__":
    app.run(debug=True)